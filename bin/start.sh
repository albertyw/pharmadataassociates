#!/bin/bash

# This is a script that can be run on a freshly setup server (see the README
# for more details) and bring it up to a production-ready state.

set -exuo pipefail
IFS=$'\n\t'

# Make compiled static files available
rm -rf static/mount/gen
cp -r static/gen static/mount

# Run supervisor to run uwsgi
supervisord -c config/supervisord.conf
