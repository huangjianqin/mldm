#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-03 15:16 
# Project: MLAndDM
# Author: huangjianqin
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # return render_template('home.html')
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('sign-ok.html', username=username)
    # abort(401)
    # return render_template('form.html', message='Bad username or password', username=username)
    return {
        "username": "aaa",
        "theme": "bbb",
    }


if __name__ == '__main__':
    app.run()
