#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 15:54 
# Project: MLAndDM
# Author: huangjianqin

from flask import Flask

app = Flask("mldm.flask")
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
