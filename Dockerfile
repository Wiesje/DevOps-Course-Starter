FROM python:3.8.5-buster as base

RUN pip install poetry

EXPOSE 8000

WORKDIR /code
COPY . /code/


FROM base as dev
RUN poetry install --no-root --no-dev
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 8000


FROM base as prod
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-root --no-dev
ENV FLASK_ENV=production
CMD poetry run gunicorn "app:create_app()" --bind 0.0.0.0:$PORT


FROM base as test
RUN apt-get update; apt-get install curl -y

#Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\
    rm ./chrome.deb

# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
    echo "Installing chromium webdriver version ${LATEST}" &&\
    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
    apt-get install unzip -y &&\
    unzip ./chromedriver_linux64.zip

RUN poetry install --no-root
ENTRYPOINT [ "poetry", "run", "pytest" ]
