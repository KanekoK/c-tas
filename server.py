import functions
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from google.cloud import translate


UPLOAD_FOLDER = r'/Users/kenya/program/c-tas/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hogehoge'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm.html', methods=['POST'])
def confirm():
    if request.method == 'POST':
        # ファイルが送信されているかどうか
        if 'upload_file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['upload_file']
        from_lang = request.form['from_lang']
        to_lang = request.form['to_lang']
        if file.filename == '':
            return redirect(request.url)
        if file and functions.allowed_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            file_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_img_path)

            text = functions.img2digit(file_img_path)
            trans_text = functions.lang_translation(text, from_lang, to_lang)
            return render_template('confirm.html', before_text=text, after_text=trans_text)
    else:
        return redirect(url_for('index'))

@app.route('/test')
def test():
    return api

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80)