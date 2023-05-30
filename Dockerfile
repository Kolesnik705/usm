FROM python:3.11.1-alpine

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR /app
COPY . /app

RUN apk update
RUN pip install --upgrade pip
RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

CMD bin/boot.sh