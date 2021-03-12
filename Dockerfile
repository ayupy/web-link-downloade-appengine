FROM gcr.io/google-appengine/python
USER root

RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

RUN venv /newapp -p python3.9

ENV VENV /newapp
ENV PATH /newapp/Scripts/activate

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

CMD gunicorn -b :8080 main:app