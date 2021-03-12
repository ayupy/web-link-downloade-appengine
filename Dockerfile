FROM gcr.io/google-appengine/python
USER root

RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /bin/sh/youtube-dl
RUN chmod a+rx /bin/sh/youtube-dl

RUN venv /env -p python3.9
RUN pip install -r requirements.txt

