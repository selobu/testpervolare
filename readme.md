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

**APi**: Navigate to http://localhost:88/docs

    Missing
    **frontEnd**: Navigate to http://localhost:xx

Repository status
-----------------

**Database Mysql - 100%**

* [x] Database. 26-11-2022
* [x] Tables. 26-11-2022
* [x] Relationships. 26-11-2022
* [x] Docker: container configuration. 26-11-2022
* [x] Docker: container test. 26-11-2022

TODO
* [ ] Contrain admin user permisions
* [ ] Generate root password dynamically
  

**Backend Fastapi gunivcorn uvicorn - 92%**

* [x] Docker: 26-11-2022
* [x] Model. 27-11-2022
* [x] Model fields validation. 27-11-2022
* [x] Github: lint - using black.  27-11-2022
* [x] Github: Added badges to show repository status.  27-11-2022 
* [x] Added two users by default, to be used to test the auth. 27-11-2022
* [x] Authentication 28-11-2022 
* [x] Registering users by themselves 28-11-2022 
* [X] Endpoints: -> Products, -> Atributos 28-11-2022 
* [x] Tests - logic implemented, it's required to increase de code coverage. 29-11-2022 
* [ ] Backend: Codecoverage config
* [x] Backend: Migrations - by using [alembic](https://alembic.sqlalchemy.org/en/latest/) 29-11-2022

TODO

* [ ] Check migrations by using alembic

**Frontend - 20%**

* [x] Frontend: Docker
* [x] Frontend: nginx
* [x] Frontend: dockerignore
* [ ] Frontend:
