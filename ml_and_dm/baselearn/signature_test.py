#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/5/30 22:55 
# Project: MLAndDM
# Author: huangjianqin
import inspect

#其实也可以自定一个函数签名(Signature, 构造函数需要Parameter实例),然后匹配合适的函数参数
from functools import wraps

from ml_and_dm.baselearn import typeassert

if __name__ == '__main__':
    @typeassert(int, str)
    # 注解
    def a(b: 'bb', c: (1, 10)) -> None:
        print(b, c)

    a(1, '2')
    print(a.__annotations__)
