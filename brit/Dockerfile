FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8

EXPOSE 8000

RUN apt-get update && apt-get install -y vim && apt-get install -y python3-pip && apt-get install -y postgresql-client

RUN apt-get install -y iputils-ping && apt-get install -y curl && apt-get install -y telnet

RUN apt-get install -y libpq-dev

RUN apt-get install sqlite3

RUN pip3 install Django 

RUN pip3 install gunicorn

# fix Django timezone error
RUN pip3 install tzdata

WORKDIR /home/

COPY . .

ARG DJANGO_ENV
ENV djangoEnv=$DJANGO_ENV

RUN python3 manage.py migrate

CMD ["sh", "-c", "ENV=${djangoEnv} gunicorn --bind 0.0.0.0:8000 brit.wsgi server --log-level debug"]
