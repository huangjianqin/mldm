#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 13:51 
# Project: MLAndDM
# Author: huangjianqin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/python?", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from mldm.flask.User import User
    Base.metadata.create_all(bind=engine)