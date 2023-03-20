FROM python:3.9.16-slim-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential zlib1g-dev libjpeg-dev libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY timetrack/ /app/
