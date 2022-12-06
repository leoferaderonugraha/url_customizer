#!/bin/sh

export FLASK_ENV=development
export FLASK_DEBUG=true
export FLASK_APP=src/py/app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=1405
export PYTHONPATH=src/py/

pip install poetry
poetry install
poetry run alembic upgrade head
poetry run flask run
