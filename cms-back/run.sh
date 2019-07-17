#!/bin/sh
if [ "$APP_ENV" == "production" ]
then
    /bin/berglas exec -- gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
elif [ "$APP_ENV" == "staging" ]
then
    /bin/berglas exec --local -- gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
else
    gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
fi
