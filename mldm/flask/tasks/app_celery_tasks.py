#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 16:12 
# Project: MLAndDM
# Author: huangjianqin
from celery import Celery
from mldm.flask.app_celery import app
def make_celery(app):
    celery = Celery(
        app.import_name + "." + "tasks.app_celery_tasks",
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task()
def add(a, b):
    return a + b

@celery.task()
def mul(a, b):
    return a * b

@celery.task()
def xsum(numbers):
    return sum(numbers)