FROM ubuntu:latest

RUN touch /test.txt

RUN apt-get update; apt-get install -y nginx
