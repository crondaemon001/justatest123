FROM ubuntu:latest

WORKDIR /app
COPY . /app

RUN apt-get update; apt-get install -y nginx
RUN apt-get install -y python3 python3-pip python3.12-venv net-tools
RUN cd /app; chmod +x promtest.py; python3 -m venv .venv; . .venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
