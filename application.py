# -*- coding: utf-8 -*-
"""
Created on 02/04/17 23:10:33

Bibliaで吐いたCSVをbibtexに変換するアプリ

@author: eqs
"""

import sys
import datetime
import flask 
import pandas as pd

# create flask app
app = flask.Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # Get file pointer of uploaded file
    f = flask.request.files['file']
    # Convert CSV text to HTML
    table = pd.io.parsers.read_csv(f)
    
    # Drop empty columns
    table.columns = ['Title', '???', 'Author', '???', 'Publisher', 'ISBN', 'Date 1', '???', '???', 'Thumbnail URL', 'Shopping URL', 'Date 2', '???', '???']
    table = table.drop('???', axis=1)

    table['ISBN'] = table['ISBN'].astype(str)

    return table.to_html()

@app.route('/')
def hello():
    return flask.render_template('upload.html')

if __name__ == '__main__':
    app.run()

