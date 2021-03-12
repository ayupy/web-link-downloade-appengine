FROM python:3.9
USER root
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install -U pip 
RUN pip install --upgrade setuptools

# run youtube-dl and ffmpeg install 
RUN apt-get update
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl
RUN apt-get ffmpeg

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:app"]
