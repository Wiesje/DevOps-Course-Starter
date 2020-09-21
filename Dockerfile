FROM python:3.8.5-buster

RUN pip install poetry

EXPOSE 8000

WORKDIR /code
COPY . /code/

RUN poetry install --no-root --no-dev

ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 8000


