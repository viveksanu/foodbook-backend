#!/bin/bash
set -e
exec gunicorn foodBook24.wsgi:application --bind 0.0.0.0:8080 --workers 3