#!/bin/bash

# Update repository
cd /var/www/website/ || exit 1
git checkout master
git pull

# Update python packages
source `which virtualenvwrapper.sh`
workon pharmadataassociates
pip install -r requirements.txt

# Restart services
sudo service nginx restart
sudo service uwsgi restart
