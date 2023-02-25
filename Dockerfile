FROM python:3.9-alpine

COPY requirements.txt /app/requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r /app/requirements.txt


COPY /library /app

WORKDIR /app


EXPOSE 8000


CMD python library/manage.py runserver 0.0.0.0:8000