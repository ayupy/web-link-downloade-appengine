from flask import Flask, render_template, request, url_for, redirect, \
    send_from_directory

import glob
import os
import pathlib
import re
import shutil

import package.dl_link as dl

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def app_run():
    global name, comb
    if request.method == 'POST':
        name = request.form.get('name')
        comb = request.form.get('convert_file')
        runydl = dl.link_web(name,comb)

        if os.path.isdir('/tmp'):
            shutil.rmtree('/tmp')
            os.mkdir('/tmp')
        else:
            os.mkdir('/tmp')

        if name != "":
            #debug
            # print(runydl.name)
            # print(runydl.comb)

            runydl.downloading()
            return redirect(url_for('app_down'))
        elif name == "":
            return render_template('index.html')
    else:
        return render_template('index.html')

def search_youtube_id(urls):
    # print('hello',urls)
    search_id = re.search(r'watch(.*)',urls)
    sample_id = "videoid"
    if search_id is None:
        return sample_id
    else:
        result_ID = search_id.group(1)[3:]
        return result_ID
    # print(search_id.group(1))
    # print(search_id.group(1)[3:])

def file_searches(file):
    # if file path is different in local and web
    # file_search = re.search(r'tmp\\(.*)',file)
    sub_file_search = re.search(r'tmp/video/(.*)',file)
    nonetype = 'None'
    if sub_file_search is None:
        return nonetype
    # print(file_search.group(1))
    # else:
    #     result_file = file_search.group(1)
    #     print(result_file)
    #     return result_file
    else:
        sub_result_file = sub_file_search.group(1)
        return sub_result_file

@app.route('/downloade/error')
def error_html():
    return render_template('error.html')


@app.route('/downloade/')
def app_down():
    # search ext file
    ext_path = 'tmp/video/'
    exts_list = ['*.webm', '*.mkv', '*.mp4', '*.mp3', '*.wav', '*.m4a']
    files_grabbed = []
    # keys is sorted var
    # keys=lambda f: os.stat(f).st_mtime
    for i in exts_list:
        files_grabbed.extend(glob.glob(ext_path+i))
    # debug
    # print(files_grabbed)
    try:
        filename = files_grabbed[-1]
        file_name = pathlib.Path(files_grabbed[-1])
        filename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
        files = file_searches(files_grabbed[-1])
        se_result = search_youtube_id(name)
        return render_template('index2.html', filename=filename, \
            video_title=filename_without_ext, yt_video_ID=se_result, \
                file=files)

    except IndexError:
        return redirect(url_for('error_html'))
# read download dir

@app.route('/downloade/delfile/',methods=['GET'])
def del_file():
    shutil.rmtree('tmp')
    os.mkdir('tmp')
    # os.remove(glob.glob('tmp/*.m4a'))
    return render_template('delfile.html')


DOWNLOAD_DIR = './'


@app.route('/downloade/<path:filename>', methods=['GET'])
def downlade_file(filename):
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run()