#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/5/30 22:55 
# Project: mldm
# Author: huangjianqin
from functools import partial

if __name__ == '__main__':
    def a(b, c):
        print(b + c)

    newA = partial(a, 100)
    newA(100)