#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/6/1 22:47 
# Project: MLandDM
# Author: huangjianqin
import numpy

if __name__ == '__main__':
    array1 = numpy.arange(2)
    print(array1)

    array2 = numpy.array([numpy.arange(2), numpy.arange(2)])
    print(array2)
    print(array2.size)
    print(array2.ndim)
    print(array2.shape)

    f64 = numpy.float64(42)
    print(f64)


    print(numpy.random.randint(0, 10, size=100))

    randJ = numpy.random.normal(5, 10, (3, 5))
    print(randJ)
    print(randJ.sum())
    print(randJ.argmin())