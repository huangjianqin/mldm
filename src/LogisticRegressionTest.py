# -*- coding: utf-8 -*-
from pyspark import SparkConf, SparkContext
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.util import MLUtils

if __name__ == "__main__":
    conf = SparkConf().setAppName("LogisticRegressionTest").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])

    # data = sc.textFile("../sample_svm_data.txt")
    # parsedData = data.map(parsePoint)
    parsedData = MLUtils.loadLibSVMFile(sc, "../sample_multiclass_classification_data.txt")

    # Build the model
    model = LogisticRegressionWithLBFGS.train(data=parsedData, iterations=10, numClasses=3)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())

    sc.stop()

    print("Training Error = " + str(trainErr))
    # print parsePoint2("1 1:-0.222222 2:0.5 3:-0.762712 4:-0.833333 ")