#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018/5/31 17:48 
# Project: mldm
# Author: huangjianqin
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, StructType, IntegerType
from pyspark.streaming import StreamingContext

if __name__ == '__main__':
    # conf = SparkConf().setAppName('pyspark-demo').setMaster("local[2]")
    # sc = SparkContext(conf=conf)
    #
    # rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8])
    # rdd2 = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # rdd3 = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #
    # sc.stop()

    ss = SparkSession.builder.appName('pyspark-sql-demo').master('local[2]').getOrCreate()

    # rdd1 = ss.sparkContext.parallelize([('a', 'a1'), ('b', 'b1')])
    #
    # schemaString = "name age"
    #
    # fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    # schema = StructType(fields)
    #
    #
    # df1 = ss.createDataFrame(rdd1, schema)
    # df1.show()

    schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])
    userDF = ss.readStream.schema(schema).json("/Users/hjq/pythonapp/mldm/data")
    userDF.select("name")
    query = userDF.writeStream.format("console").start()
    print(query.recentProgress)
    query.awaitTermination()

    ss.stop()