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

## Docker-compose support

To build the Docker images, run the following command:

        docker-compose build

To start the Docker containers, run the following command:

        docker-compose up

The database is created in a separate container and will persist even after the containers are stopped. This means that you can stop and start the containers without losing your data.

## OpenAPI Swagger support

Once the server is up and running, you can view the API endpoints documentation by navigating to the following URLs in your web browser:

For OpenAPI specification in JSON format:

      http://localhost:8000/schema

For API documentation in a user-friendly format:

      http://localhost:8000/schema/redoc

For API documentation in a Swagger UI format:

      http://localhost:8000/schema/swagger-ui

Using these URLs, you can easily explore the API endpoints and their expected request and 
response formats.
