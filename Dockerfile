FROM python:3.8.5-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

EXPOSE 8000

COPY . /code/

RUN source setup.sh

ENTRYPOINT flask run -h 0.0.0.0 -p 8000


