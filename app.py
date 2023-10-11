#python -m venv c:\path\to\myenv
#source venv/bin/activate
#flask run --debug
#flask run -h localhost -p 3009 --debug

from flask import Flask,render_template,request, make_response, send_file, jsonify
from werkzeug.utils import secure_filename
import json,os
import pandas as pd
import numpy as np
#from flask.ext.login import LoginManager,login_user ,UserMixin

app=Flask(__name__)
app.secret_key='this is my secret'

#if __name__=='__main__':
#        app.run(debug=True)
#        app.run(debug=True,port=int(os.getenv('PORT', 4001)))
#        app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 4444)))

@app.route('/')
def home():
	return "Hello, check address! \n \\simple.png \n \\simdata\n \\kidu"

@app.route('/kidu', methods=['GET','POST'])
def kidu():
    return render_template("kidu.htm",data = 'None')


def upload_file():
    if request.method == 'POST':
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file = request.files['file']
            return secure_filename(file.filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


