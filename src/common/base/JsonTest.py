#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2017/9/3 21:54
# Project: MLandDM
# Author: huangjianqin
import json

if __name__ == '__main__':
    jsonStr = '{"a":1, "b":[{"b1":"b1", "b2":"b2"}]}'
    jsonO = json.loads(jsonStr)
    jsonStr2 = json.dumps(jsonO)
    jsonStr3 = {"a":1, "b":[{"b1":"b1", "b2":"b2"}]}
    print jsonStr3['a']
    print json.dumps(jsonO)
    print jsonStr2.__eq__(jsonStr)