FROM python:3.8-slim-buster
USER root

RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

WORKDIR /app

copy requirements.txt requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY . .

CMD gunicorn -b :8080 main:app