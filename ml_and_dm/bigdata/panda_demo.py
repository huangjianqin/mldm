#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/6/4 21:34 
# Project: MLAndDM
# Author: huangjianqin
import math
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({'key':['a','b','c'],'data1':[1,None,3],'data2':[4,5,6]})
    print(df)
    # for idx, item in df.iterrows():
    #     print(idx)
    #     print(item)
    # print(df[:1])
    # print(df['key'])

    # print(df['key'].describe())
    # print(df['data1'].describe())
    # print(df['data1'].fillna(0, inplace=True))

    # df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'data1': [1, 2, 3]})
    # df2 = pd.DataFrame({'key': ['a', 'b', 'c'], 'data2': [4, 5, 6]})
    # df3 = pd.merge(df1, df2)
    # print(df3)

    # df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'data': [1, 2, 3]})
    # df2 = pd.DataFrame({'key': ['a', 'b', 'c'], 'data': [4, 5, 6]})
    # df3 = pd.concat([df1, df2])
    # print(df3)

    # df = pd.DataFrame({'key': ['a', 'b', 'c'], 'data1': [1, 2, 3]})
    # print(df)
    # df['data1'] = df['data1'].apply(lambda x: math.sin(x))
    # print(df)

    # def testme(x):
    #     print(x['data1'], x['data2'])
    #     return x['data1'] + x['data2']
    #
    #
    # df = pd.DataFrame({'key': ['a', 'b', 'c'], 'data1': [1, 2, 3], 'data2': [4, 5, 6]})
    # print(df)
    # df['data3'] = df.apply(testme, axis=1)
    # print(df)

