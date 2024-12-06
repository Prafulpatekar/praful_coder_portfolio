Project Setup
=============

POETRY Setup Instructions
==========================
1. `poetry init`
2. `poetry add ` 
3. `poetry install`

Run command using Poetry 
========================
1. `poetry run python manage.py runserver` here 'python manage.py runserver' is the command we are running inside poetry. Poetry ensures the consistency.

Makefile commands
=================
1. `choco install make` to install make package in windows
2. `make <target>` to run any command added in Makefile

Setup django settings for local
===============================
1. `mkdir local`
2. `cp src/myportfolio/settings/template/settings.dev.py ./local/settings.dev.py`