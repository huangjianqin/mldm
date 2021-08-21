#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 13:51 
# Project: MLAndDM
# Author: huangjianqin
from flask import Flask, jsonify

from mldm.flask.User import User
from mldm.flask.database import db_session, init_db

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/insert", methods=["GET"])
def insert():
    u = User('admin1', 'admin1@localhost')
    db_session.add(u)
    db_session.commit()
    return {"code": 200}

@app.route("/query", methods=["GET"])
def query():
    return jsonify([user.json() for user in User.query.all()])


if __name__ == '__main__':
    init_db()
    app.run()