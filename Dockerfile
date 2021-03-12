FROM gcr.io/google-appengine/python
USER root

RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

RUN venv /env -p python3.7

ENV VIRTUAL_ENV /env
ENV PATH /env/bin/activate

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
