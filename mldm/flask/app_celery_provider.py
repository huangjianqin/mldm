#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-02-04 17:00 
# Project: MLAndDM
# Author: huangjianqin
from celery import group, chain, chord

from mldm.flask.tasks.app_celery_tasks import add, mul, xsum

if __name__ == '__main__':
    print(group(add.s(i, i) for i in range(10))().get())
    print(chain(add.s(4, 4) | mul.s(8))().get())
    print(chord((add.s(i, i) for i in range(10)), xsum.s())().get())
    print(chain (group(add.s(i, i) for i in range(10)) | xsum.s())().get())