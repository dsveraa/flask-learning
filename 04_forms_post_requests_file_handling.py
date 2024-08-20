import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('04_index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'neuralnine' and password == 'password':
            return 'Success'
        else:
            return 'Fail'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)