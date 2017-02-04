# -*- coding: utf-8 -*-
"""
Created on 02/04/17 23:10:33

Bibliaで吐いたCSVをbibtexに変換するアプリ

@author: eqs
"""

import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

