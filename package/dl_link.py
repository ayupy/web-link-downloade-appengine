import subprocess

class link_web():
    def __init__(self,name,comb):
        self.outtmpl = '%(title)s.%(ext)s'
        # downlode file path
        self.path = 'tmp/video/'
        # youtube-dl comand and options
        self.name = name
        self.comb = comb
        base_format = f'youtube-dl "{self.name}" -o "{self.path+self.outtmpl}"'
        audio = f'--extract-audio --audio-format'
        video = f'-f bestvideo+bestaudio --merge-output-format'
        self.audio_only = f'{base_format} {audio}'
        self.video = f'{base_format} {video}'

    def download(self):
        self.select_comb()

    def downloading(self):
        self.download()

    def select_comb(self):
        ext = ['webm', 'mkv', 'mp4', 'mp3', 'wav', 'm4a']
        if self.comb == 'mp3':
            subprocess.run(f'{self.audio_only} {ext[3]}',shell=True)
        elif self.comb == 'mp4':
            subprocess.run(f'{self.video} {ext[2]}',shell=True)
        elif self.comb == 'm4a':
            subprocess.run(f'{self.audio_only} {ext[5]}',shell=True)
        elif self.comb == 'webm':
            subprocess.run(f'{self.video} {ext[0]}',shell=True)
        elif self.comb == 'wav':
            subprocess.run(f'{self.audio_only} {ext[4]}',shell=True)
        elif self.comb == 'mkv':
            subprocess.run(f'{self.video} {ext[1]}',shell=True)
