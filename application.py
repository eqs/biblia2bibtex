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

# template string for bibtex
bibtex_template = """
@book{{{ISBN}, <br/>
\tauthor=\"{author}\", <br/>
\ttitle=\"{title}\", <br/>
\tpublisher=\"{publisher}\", <br/>
\tyear=\"{year}\"<br/>
}}<br/>
<br/>
"""

# create flask app
app = flask.Flask(__name__)

def to_bibtex(table):
    """表をbibtexに変換する関数
    :param table: 本の表
    :return: bibtex化した文字列
    """
    text = ""
    for k, row in table.iterrows():
        text += bibtex_template.format(
            ISBN=row['ISBN'], 
            author=row['Author'].replace("/",  " and "), 
            title=row['Title'], 
            publisher=row['Publisher'], 
            year=''
        )
    return text

@app.route('/bibtex.bib', methods=['GET', 'POST'])
def upload_file():
    # Get file pointer of uploaded file
    f = flask.request.files['file']
    # Convert CSV text to HTML
    table = pd.io.parsers.read_csv(f, dtype=str, keep_default_na=False, na_values=['***'])
    
    # Drop empty columns
    table.columns = ['Title', '???', 'Author', '???', 'Publisher', 'ISBN', 'Date 1', '???', '???', 'Thumbnail URL', 'Shopping URL', 'Date 2', '???', '???']
    table = table.drop('???', axis=1)

    table['ISBN'] = table['ISBN'].astype(str)

    return to_bibtex(table)

@app.route('/')
def hello():
    return flask.render_template('upload.html')

if __name__ == '__main__':
    app.run()

