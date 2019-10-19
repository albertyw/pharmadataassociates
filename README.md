# Pharma Data Associates Website

[ ![Codeship Status for albertyw/pharmadataassociates](https://codeship.com/projects/7e5b4e40-3428-0134-823e-26e7891ba113/status?branch=master)](https://codeship.com/projects/164911)
[![Updates](https://pyup.io/repos/github/albertyw/pharmadataassociates/shield.svg)](https://pyup.io/repos/github/albertyw/pharmadataassociates/)
[![Code Climate](https://codeclimate.com/github/albertyw/pharmadataassociates/badges/gpa.svg)](https://codeclimate.com/github/albertyw/pharmadataassociates)
[![Test Coverage](https://codeclimate.com/github/albertyw/pharmadataassociates/badges/coverage.svg)](https://codeclimate.com/github/albertyw/pharmadataassociates/coverage)

https://www.pharmadataassociates.com/

PDA Website V2

Development
-----------

### Setup (using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)):

```bash
mkvirtualenv pharmadataassociates -p python3.8
pip install -r requirements.txt
pip install -r requirements-test.txt
ln -s .env.development .env

# Install shellcheck
# brew install shellcheck
# sudo apt-get install shellcheck
```

### Spinning up the server:

```bash
python app/serve.py
```

### Running tests:

```bash
flake8
mypy app --ignore-missing-imports
shellcheck --exclude=SC1091 bin/*
coverage run -m unittest discover
```

### CI/CD

This repo uses:

```bash
# Switch to python 3
pyenv local 3.8
pip install -r requirements.txt
pip install -r requirements-test.txt
ln -s .env.development .env

# Test
flake8
mypy app --ignore-missing-imports
shellcheck --exclude=SC1091 bin/*
coverage run -m unittest discover
coverage report
codeclimate-test-reporter

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

```bash
bin/setup.sh
```

### Deploment

```bash
bin/deploy.sh
```
