FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
# Install build requirements
RUN apk add --no-cache mariadb-connector-c-dev \
    && apk add --no-cache --virtual .build-deps build-base mariadb-dev jpeg-dev zlib-dev

COPY requirements.txt /requirements.txt
# Enable manylinux1 support, so that we can get Wheels for more packages: https://github.com/pypa/pip/issues/3969#issuecomment-247381915
#RUN echo 'manylinux1_compatible = True' > /usr/local/lib/python3.7/site-packages/_manylinux.py \
#    && pip install --prefix=/install --no-warn-script-location -r /requirements.txt
RUN pip install --prefix=/install --no-warn-script-location -r /requirements.txt

FROM base
# Install requirements for packages
RUN apk add --no-cache mariadb-connector-c-dev libjpeg
COPY --from=builder /install /usr/local

RUN adduser -D python
USER python
RUN mkdir -p /home/python/app
WORKDIR /home/python/app

COPY --chown=python:python . .

CMD ["sh", "run.sh"]