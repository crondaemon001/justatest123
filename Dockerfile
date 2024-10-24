FROM ubuntu:latest

RUN touch /test.txt

COPY . /app

RUN ls -la /app
RUN apt-get install -y python3 python3-pip python3.12-venv net-tools
RUN cd /app; chmod +x promtest.py; python3 -m venv .venv; . .venv/bin/activate
RUN pip install Flask
RUN pip install prometheus-client

RUN apt-get update; apt-get install -y nginx
