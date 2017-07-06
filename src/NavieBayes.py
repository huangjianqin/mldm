# -*- coding:utf-8 -*-
from pyspark import SparkConf, SparkContext
from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint

if __name__ == "__main__":
    conf = SparkConf().setAppName("NavieBayes").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    def parseLine(line):
        parts = line.split(',')
        label = float(parts[0])
        features = Vectors.dense([float(x) for x in parts[1].split(' ')])
        return LabeledPoint(label, features)


    data = sc.textFile('../sample_naive_bayes_data.txt').map(parseLine)

    # Split data aproximately into training (60%) and test (40%)
    training, test = data.randomSplit([0.6, 0.4], seed=0)

    # Train a naive Bayes model.
    model = NaiveBayes.train(training, 1.0)

    # Make prediction and test accuracy.
    predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / test.count()

    print accuracy