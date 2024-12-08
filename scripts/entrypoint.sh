#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python -m myportfolio.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

# FOr django channels
# exec poetry run daphne cooking_core.project.asgi:application -p 8000 -b 0.0.0.0

exec poetry run gunicorn myportfolio.myportfolio.wsgi:application -p 8000 -b 0.0.0.0
