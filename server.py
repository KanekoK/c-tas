from flask import Flask, render_template, request, redirect, url_for
import app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm.html', methods=['POST'])
def confirm():
    if request.method == 'POST':
        return request.form
        # return render_template('confirm.html')
    else:
        return redirect(url_for('index'))

@app.route('/test')
def test():
    return api

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80)