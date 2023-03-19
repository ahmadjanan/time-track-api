FROM python:3.9.16-slim-bullseye
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

RUN apt-get update && apt-get install -y build-essential zlib1g-dev libjpeg-dev libpq-dev && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY timetrack /usr/src/app/

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
