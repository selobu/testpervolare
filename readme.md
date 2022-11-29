# Pervolare test
![Lint](https://github.com/selobu/testpervolare/actions/workflows/black.yml/badge.svg)
![tests](https://github.com/selobu/testpervolare/actions/workflows/test.yml/badge.svg)
![codecov](https://codecov.io/gh/selobu/testpervolare/branch/master/graph/badge.svg)
![Codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)

Backend [![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/downloads/release/python-390/)

Usage
======

You should use it with [Docker](https://www.docker.com/):

    $ docker compose -f "docker-compose.yml" down 
    $ docker compose -f "docker-compose.yml" up -d --build

**APi**: Navigate to http://localhost:88/docs

**frontEnd**: Navigate to http://localhost or http://localhost:80 

Repository status
-----------------

**Database Mysql - 100%**

* [x] Database.
* [x] Tables.
* [x] Relationships.
* [x] Docker: container configuration.
* [x] Docker: container test.

TODO
* [ ] Contrain admin user permisions
* [ ] Generate root password dynamically
  

**Backend Fastapi gunicorn uvicorn - 92%**

* [x] Docker.
* [x] Model.
* [x] Model fields validation.
* [x] Github: lint - using black.
* [x] Github: Added badges to show repository status.
* [x] Added two users by default, to be used to test the auth.
* [x] Authentication.
* [x] Registering users by themselves. 
* [X] Endpoints: -> Products -> Atributos 
* [x] Tests - logic implemented, it's required to increase de code coverage. 
* [ ] Backend: Codecoverage config
* [x] Backend: Migrations - by using [alembic](https://alembic.sqlalchemy.org/en/latest/)

TODO

* [ ] Check migrations by using alembic

**Frontend - 20%**

* [x] Frontend: Docker
* [x] Frontend: nginx
* [x] Frontend: dockerignore
* [ ] Frontend:
