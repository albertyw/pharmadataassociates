# Pharma Data Associates Website

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/pharmadataassociates/status.svg)](https://drone.albertyw.com/albertyw/pharmadataassociates)
[![Maintainability](https://qlty.sh/gh/albertyw/projects/pharmadataassociates/maintainability.svg)](https://qlty.sh/gh/albertyw/projects/pharmadataassociates)
[![Code Coverage](https://qlty.sh/gh/albertyw/projects/pharmadataassociates/coverage.svg)](https://qlty.sh/gh/albertyw/projects/pharmadataassociates)
[![Varsnap Status](https://www.varsnap.com/project/8aa438e7-9242-485b-ac1b-c0bab8630069/varsnap_badge.svg)](https://www.varsnap.com/project/8aa438e7-9242-485b-ac1b-c0bab8630069/)

https://www.pharmadataassociates.com/

PDA Website V2

Development
-----------

### Setup
Using [python venv](https://docs.python.org/3/library/venv.html) and
[direnv](https://github.com/direnv/direnv)

```bash
python3.13 -m venv env
printf "source env/bin/activate\nunset PS1\n" > .envrc
direnv allow
pip install -e .[test]
ln -s .env.development .env
npm install

# Install shellcheck
# brew install shellcheck
# sudo apt-get install shellcheck
```

### Spinning up the server:

```bash
npm run build:dev
python app/serve.py
```

### Running tests:

```bash
ruff check .
mypy .
shellcheck --exclude=SC1091 bin/*.sh
coverage run -m unittest discover
npm test
```

### CI/CD

This repo uses:

```bash
# Switch to python 3
pyenv local 3.13
pip install -e .[test]
ln -s .env.development .env

# Test
ruff check .
mypy .
shellcheck --exclude=SC1091 bin/*.sh
coverage run -m unittest discover
coverage report
npm test

# Deployment
ssh ubuntu@pharmadataassociates.com pharmadataassociates/bin/deploy.sh
```

### Building and starting the docker container

```bash
docker build -t pharmadataassociates:test .
docker run -t -i -p 127.0.0.1:5001:5000 pharmadataassociates:test
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
