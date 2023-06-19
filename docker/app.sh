#!/bin/bash

poetry run alembic upgrade head

cd src

poetry run gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000