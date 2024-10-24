FROM ubuntu:latest

RUN touch /test.txt

COPY . /app

RUN ls -la /app

RUN apt-get update; apt-get install -y nginx
