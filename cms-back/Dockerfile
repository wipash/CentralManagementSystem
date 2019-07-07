FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
# Install requirements for mysqlclient
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps build-base mariadb-dev

COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
# Install requirements for mysqlclient
RUN apk add --no-cache mariadb-connector-c-dev
COPY --from=builder /install /usr/local

RUN adduser -D python
USER python
RUN mkdir -p /home/python/app
WORKDIR /home/python/app

COPY --chown=python:python . .

CMD ["sh", "run.sh"]