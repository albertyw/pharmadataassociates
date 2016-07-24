#!/bin/bash

# Update repository
cd /var/www/website/
git checkout master
git pull

# Update python packages
source `which virtualenvwrapper.sh`
workon pharmadataassociates
pip install -r requirements.txt

# Configure settings
ln -sf .env.production .env

# Restart services
sudo service nginx restart
sudo service uwsgi restart
