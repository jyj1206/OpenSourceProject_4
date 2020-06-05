#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

url=""
@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/info', methods=['POST'])
def urlanalysis():
    if request.method == 'POST':
        return render_template('info.html',url=url)

if __name__ == '__main__':
    app.run()
