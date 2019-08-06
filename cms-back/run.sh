#!/bin/sh
if [ "$APP_ENV" = "production" ]
then
    /bin/berglas exec -- gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
elif [ "$APP_ENV" = "testing" ] || [ "$APP_ENV" = "staging" ]
then
    /bin/berglas exec --local -- gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
elif [ "$APP_ENV" = "dev" ]
then
    /bin/berglas exec --local -- python manage.py runserver "0.0.0.0:$PORT"
else
    gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
fi
