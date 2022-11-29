# Pervolare test
![Lint](https://github.com/selobu/testpervolare/actions/workflows/black.yml/badge.svg)
![tests](https://github.com/selobu/testpervolare/actions/workflows/test.yml/badge.svg)
![codecov](https://codecov.io/gh/selobu/testpervolare/branch/master/graph/badge.svg)
![Codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)

Backend [![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)](https://www.python.org/downloads/release/python-390/)

Usage
======

You should use it with [Docker](https://www.docker.com/):

    $ docker compose -f "docker-compose.yml" down 
    $ docker compose -f "docker-compose.yml" up -d --build

**APi**: Navigate to http://localhost/docs

    Missing
    **frontEnd**: Navigate to http://localhost:xx

Repository status
-----------------

* [x] MySQL: Database. 26-11-2022
* [x] MySQL: Tables. 26-11-2022
* [x] MySQL: Relationships. 26-11-2022
* [x] Docker: Database container configuration. 26-11-2022
* [x] Docker: Database container test. 26-11-2022
* [x] Docker: Backend. 26-11-2022
* [x] Backend: model. 27-11-2022
* [x] Backend: Model fields validation. 27-11-2022
* [x] Github: lint - using black.  27-11-2022
* [x] Github: Added badges to show repository status.  27-11-2022 
* [x] Backend: Added two users by default, to be used to test the auth. 27-11-2022
* [x] Backend: Authentication 28-11-2022 
* [x] Backend: Registering users by themselves 28-11-2022 
* [X] Backend: Endpoints: -> Products, -> Atributos 28-11-2022 
* [x] Backend: Tests - logic implemented, it's required to increase de code coverage. 29-11-2022 
* [ ] Backend: Codecoverage config
* [x] Backend: Migrations - by using [alembic](https://alembic.sqlalchemy.org/en/latest/) 29-11-2022 
* [x] Frontend: Docker
* [x] Frontend: nginx
* [x] Frontend: dockerignore
* [ ] Frontend:
