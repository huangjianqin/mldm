#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 13:56 
# Project: MLAndDM
# Author: huangjianqin
import json

from sqlalchemy import Column, Integer, String

from mldm.flask.database import Base

class User(Base):
    # 定义表名, 可定义, 也不定义
    __tablename__ = 'User'
    # 字段定义
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

    def json(self):
        return {"id":self.id, "name":self.name, "email":self.email}