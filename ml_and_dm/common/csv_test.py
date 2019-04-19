#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2017/9/3 22:34
# Project: MLAndDM
# Author: huangjianqin
import csv

if __name__ == '__main__':
    print(csv.list_dialects)
    with open('airlineData.csv', "rb") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['WORK_CITY'])