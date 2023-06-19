FROM python:3.11

RUN mkdir /app

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install --no-root

RUN chmod a+x docker/*.sh

#WORKDIR src

#CMD poetry run gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000