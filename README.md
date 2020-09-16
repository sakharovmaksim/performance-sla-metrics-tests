Sample of Performance SLA metrics tests engine
========================================================

## Description

### Runner configuration 
Configs in yaml-files and ammos in txt-files in `tank_config_templates` dir

### Tests configuration
Requests and 'bullets' configurating in txt-files, which uses by tests runner. In bullet describes endpoints, which 
need to test.

## Run performance tests!
### In special Linux container or host with Yandex Tank, installed by PyPi
1. Install Yandex Tank Application in docker container or host with Linux (Ubuntu) 
https://yandextank.readthedocs.io/en/latest/install.html#installation-from-pypi
2. Set performance target host URL in `pytest-xxx.ini` config  
3. Set your Overload token in `token.txt` file showing for tests performance statistics
4. RUN: `pipenv run pytest tests -c tests/pytest-dev.ini`

## Docs
https://yandextank.readthedocs.io/en/latest/index.html