#!/bin/sh
gunicorn djangocloudrun.wsgi -w 2 -b ":$PORT"
