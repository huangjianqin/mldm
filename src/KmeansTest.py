# -*- coding:utf-8 -*-
from array import array
from math import sqrt

from pyspark import SparkConf, SparkContext
from pyspark.mllib.clustering import KMeans

def error(point, clusters):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x ** 2 for x in (point - center)]))

def run(parsedData, k):
    clusters = KMeans.train(parsedData, k, maxIterations=20,
                            runs=10, initializationMode="random")

    WSSSE = parsedData.map(lambda point: error(point, clusters)).reduce(lambda x, y: x + y)
    # print("Within Set Sum of Squared Error = " + str(WSSSE))
    return WSSSE

if __name__ == '__main__':
    conf = SparkConf().setAppName("Kmeans").setMaster("local[8]")
    sc = SparkContext(conf=conf)

    data = sc.textFile("../data.txt")
    parsedData = data.map(lambda line: [float(x) for x in line.split(' ')])

    results = []
    for i in range(5, 5, 5):
        WSSSE = run(parsedData, i)
        results.append(str(i) + "," + str(WSSSE))

    sc.stop()

    for result in results:
        print result