#!/bin/bash

# This script will build and deploy a new docker image

set -exuo pipefail
IFS=$'\n\t'

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "$DIR"/..

source .env

if [ "$ENV" = "production" ]; then
    # Update repository
    git checkout master
    git fetch -tp
    git pull
fi

# Build and start container
docker build -t "pharmadataassociates:$ENV" .
docker network inspect "pharmadataassociates" &>/dev/null ||
    docker network create --driver bridge "pharmadataassociates"
docker stop "pharmadataassociates" || true
docker container prune --force --filter "until=168h"
docker image prune --force --filter "until=168h"
docker volume prune --force
docker container rm "pharmadataassociates" || true
docker run \
    --detach \
    --restart always \
    --publish="127.0.0.1:5001:5001" \
    --network="pharmadataassociates" \
    --mount type=bind,source="$(pwd)"/app/static,target=/var/www/app/app/static \
    --mount type=bind,source="$(pwd)"/logs,target=/var/www/app/logs \
    --name "pharmadataassociates" "pharmadataassociates:$ENV"

if [ "$ENV" = "production" ]; then
    # Cleanup docker
    docker image prune --force --filter "until=168h"

    # Update nginx
    sudo service nginx reload
fi
