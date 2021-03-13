# README
![img_1](https://user-images.githubusercontent.com/80331087/111036261-b6e3ab00-8461-11eb-9051-81678070d9df.png)

# web_link_downloader
web_link_downloader is downloade video of the web link.
you can use Corresponds some web links.

this code use flask app.

you can try local or google App engine site.


# starting app
if you have a python program,you can install requirements.txt and use it in a virtual environment.

pip install command

```

pip install -r requirements.txt

```

# install youtube-dl and ffmpeg on windown or mac

web_link_downloader need youtube-dl and ffmpeg.

install youtube-dl

linux,macOS:

```
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```

windows:

go to https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme


install ffmpeg

linux,macOS:
use brew command

```
brew install ffmpeg
```

use apt-get command

```
apt-get install ffmpeg
```


# run python 
run python3 or python command.

```
python app.py
```

then,move localhost,

you try some video link URl to paste text and choose video extension file.

example Corresponds some web site,  

-youtube:https://www.youtube.com/

-twitter:https://twitter.com/

-instagram:https://www.instagram.com/

-facebook:https://www.facebook.com/

-...others site https://ytdl-org.github.io/youtube-dl/supportedsites.html

# save file

web_link_downloader is default save file path ./tmp/video/

if no tmp directory,make tmp directory in Current directory


# web service
if you don't have python program,you can visit my web service.

web app site is google App engine

if you use App engine,you need Dockerfile and app.yaml.

here is site:https://web-link-downloade-appengine-dot-images-pro-30.df.r.appspot.com/

# LICENCE
The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.

