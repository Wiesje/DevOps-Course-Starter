FROM python:3.8.5-buster as base

RUN pip install poetry

EXPOSE 8000

WORKDIR /code
COPY . /code/

RUN poetry install --no-root --no-dev

FROM base as dev
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 8000

FROM base as prod
ENV FLASK_ENV=production
ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0:8000
