FROM gcr.io/google-appengine/python
USER root

RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

RUN venv /env -p python3.9

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD requirements.txt
RUN pip install -r requirements.txt

CMD gunicorn -b :8080 main:app