FROM gcr.io/google-appengine/python

RUN apt-get update
RUN apt-get install python-virtualenv
RUN venv /env -p python3.7

ENV VIRTUAL_ENV /env
ENV source /env/bin/activate

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

ADD . /app
WORKDIR /app

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:app"]
