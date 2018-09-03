#!/bin/bash

# This script will build and deploy a new docker image

# Update repository
cd pharmadataassociates || exit 1
git checkout master
git fetch -tp
git pull

# Build and start container
docker build -t pharmadataassociates:production .
docker stop pharmadataassociates || echo
docker container prune -f
docker run --detach --restart always -p 127.0.0.1:5001:5001 --name pharmadataassociates pharmadataassociates:production

# Cleanup docker
docker image prune -f

# Update nginx
sudo service nginx reload
