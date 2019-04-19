#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/3/16 11:15 
# Project: MLAndDM
# Author: huangjianqin
import inspect
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            # 解析成参数签名
            btypes = sig.bind_partial(*ty_args, **ty_kwargs).arguments

            # 解析成参数签名
            for arg_name, obj in sig.bind(*args, **kwargs).arguments.items():
                if arg_name in btypes:
                    if not isinstance(obj, btypes[arg_name]):
                        raise TypeError('"%s" must be "%s"' % (arg_name, btypes[arg_name]))

            return func(*args, **kwargs)
        return wrapper
    return decorator

def coroutineHelper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wrapper