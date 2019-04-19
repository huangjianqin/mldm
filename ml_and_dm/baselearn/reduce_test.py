#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/5/30 22:55 
# Project: MLAndDM
# Author: huangjianqin
from functools import reduce

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6,]
    l2 = [2, 3, 4, 5, 6, 7,]

    for x in map(lambda x, y: x + y, l1, l2):
        print(x, end=',')

    print('')

    print(reduce(lambda x, y: x + y, l1))