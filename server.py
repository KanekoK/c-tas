from flask import Flask, render_template, request
from app import api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm.html')
def confirm():
    return render_template('confirm.html')

@app.route('/test')
def test():
    return api

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80)