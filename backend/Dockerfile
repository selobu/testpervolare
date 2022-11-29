FROM asdkant/fastapi-hello-world
LABEL "maintainer"="Sebastian López Buritica <selobu at gamil dot com>"
RUN  pip install --upgrade pip
RUN  pip install pydantic[email] python-multipart
RUN  pip install sqlalchemy
RUN  pip install sqlmodel
RUN  pip install PyMySQL
RUN  pip install cryptography
WORKDIR /
COPY ./start.sh  ./start.sh
WORKDIR /app