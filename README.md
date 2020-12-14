Sample of Performance SLA metrics tests engine
========================================================

## Description

### Runner configuration 
Configs in yaml-files and ammos in txt-files in `tank_config_templates` dir

### Tests configuration
Requests and 'bullets' configurating in txt-files, which uses by tests runner. In bullet describes endpoints, which 
need to test.

## Run performance tests!
### On your local machine
1. Install Docker engine https://www.docker.com/get-started
2. Set target host URL for performance testing in `pytest-xxx.ini` config  
3. Set your Overload token in `token.txt` file showing for tests performance statistics (https://overload.yandex.net/login/?next=/)
4. RUN: `pipenv run pytest tests -c tests/pytest-dev.ini` with `pytest-dev.ini` config

## Docs
https://yandextank.readthedocs.io/en/latest/index.html