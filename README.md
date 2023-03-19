# Time Track

A REST API for a multi-user and multi-project work time tracking
application using Django and Django Rest Framework.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

-   Python 3.9.x
-   Pipenv (you can install it by running `pip install pipenv`)

## Quickstart

1. Set up a Python virtual environment and install the required Python dependencies:

        pipenv install

2. Create `.env` configuration file based on `env.sample`:

        cp sample.env .env
        vim .env

3. Move to the Django project directory:

        cd timetrack

5. Run migrations:

        pipenv run python manage.py migrate

6. Run the server:

        pipenv run python manage.py runserver


## Running tests

    pipenv run pytest

To view the coverage report

    pipenv run coverage run -m pytest
    pipenv run coverage report

## Docker support

Build the docker image with:

        docker build -t time-track .

The default command is to start the web server. Run the image
with `-P` docker option to expose the internal port and check the exposed
port with `docker ps`:

        docker run --env-file .env -p 8000:8000 time-track

Note that any changes inside the container will be lost. For that reason, using a SQLite database within a container will
have no effect. If you want to use SQLite with docker, mount a docker volume and place the SQLite database inside it.
