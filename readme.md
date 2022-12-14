# Pervolare test
![Lint](https://github.com/selobu/testpervolare/actions/workflows/black.yml/badge.svg)
![tests](https://github.com/selobu/testpervolare/actions/workflows/test.yml/badge.svg)
![Codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)
![codecov](https://codecov.io/gh/selobu/testpervolare/branch/master/graph/badge.svg)

Backend [![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/downloads/release/python-390/)

## Usage

You should use it with [Docker](https://www.docker.com/):

    $ docker compose -f "docker-compose.yml" down 
    $ docker compose -f "docker-compose.yml" up -d --build

## Mapped ports

**Mysql**: Navigate to http://localhost:3307

**APi**: Navigate to http://localhost:88/docs 

**frontEnd**: Navigate to http://localhost or http://localhost:80 

## Repository status

Item   | status | pending
----|-----|------
Databse |  ![100%](https://progress-bar.dev/100) | Adjust permisions
Backend | ![92%](https://progress-bar.dev/92) | increase pytest code coverage
Docker | ![90%](https://progress-bar.dev/90) | Adjust healthcheck conditions
FrontEnd | ![40%](https://progress-bar.dev/40) | axios, memory, components, and so on..


### Database Mysql

* [x] Database.
* [x] Tables.
* [x] Relationships.
* [x] Docker: container configuration.
* [x] Docker: container test.

 TODO
* [ ] Constrain admin user permisions
* [ ] Generate root password dynamically
  

### Backend Fastapi gunicorn uvicorn

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

### Frontend

* [x] Docker
* [x] nginx
* [x] dockerignore
* [x] vuetify
* [x] Router
* [x] axios
* [ ] Sign in
* [ ] Sign up
* [ ] Product list
* [ ] Product list filter
* [ ] Product delete
* [ ] Attirute list
* [ ] Attribute list filter
* [ ] Attribute delete

**Video description**

Spanish repository video description

[![image](http://img.youtube.com/vi/maRKriel5ao/0.jpg)](https://youtu.be/maRKriel5ao)
