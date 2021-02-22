# Pharma Data Associates Website

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/pharmadataassociates/status.svg)](https://drone.albertyw.com/albertyw/pharmadataassociates)
[![Updates](https://pyup.io/repos/github/albertyw/pharmadataassociates/shield.svg)](https://pyup.io/repos/github/albertyw/pharmadataassociates/)
[![Code Climate](https://codeclimate.com/github/albertyw/pharmadataassociates/badges/gpa.svg)](https://codeclimate.com/github/albertyw/pharmadataassociates)
[![Test Coverage](https://codeclimate.com/github/albertyw/pharmadataassociates/badges/coverage.svg)](https://codeclimate.com/github/albertyw/pharmadataassociates/coverage)
[![Varsnap Status](https://www.varsnap.com/project/8aa438e7-9242-485b-ac1b-c0bab8630069/varsnap_badge.svg)](https://www.varsnap.com/project/8aa438e7-9242-485b-ac1b-c0bab8630069/)

https://www.pharmadataassociates.com/

PDA Website V2

Development
-----------

### Setup (using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)):

```bash
mkvirtualenv pharmadataassociates -p python3.9
pip install -r requirements.txt
pip install -r requirements-test.txt
ln -s .env.development .env
npm install

# Install shellcheck
# brew install shellcheck
# sudo apt-get install shellcheck
```

### Spinning up the server:

```bash
npm run minify
python app/serve.py
```

### Running tests:

```bash
flake8
mypy app --ignore-missing-imports --strict
shellcheck --exclude=SC1091 bin/*.sh
coverage run -m unittest discover
npm test
```

### CI/CD

This repo uses:

```bash
# Switch to python 3
pyenv local 3.9
pip install -r requirements.txt
pip install -r requirements-test.txt
ln -s .env.development .env

# Test
flake8
mypy app --ignore-missing-imports --strict
shellcheck --exclude=SC1091 bin/*.sh
coverage run -m unittest discover
coverage report
codeclimate-test-reporter
npm test

# Deployment
ssh ubuntu@pharmadataassociates.com pharmadataassociates/bin/deploy.sh
```

### Building and starting the docker container

```bash
docker build -t pharmadataassociates:test .
docker run -t -i -p 127.0.0.1:5001:5001 pharmadataassociates:test
```

Production
----------

### Setup

Run this once on a new server to set up the web app:

```bash
bin/setup.sh
```

### Deployment

Run this every time for a new commit to the repository:

```bash
bin/deploy.sh
```
