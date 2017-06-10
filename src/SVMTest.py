# -*- conding: utf-8 -*-
from pyspark import SparkConf, SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

if __name__ == "__main__":
    conf = SparkConf().setAppName("SVMTest").setMaster("local[4]")
    sc = SparkContext(conf=conf)

    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])


    data = sc.textFile("../sample_svm_data.txt")
    parsedData = data.map(parsePoint)

    # Build the model
    model = SVMWithSGD.train(parsedData, iterations=1000)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())

    # def printR((v, p)):
    #     print str(v)
    #     print str(p)
    #     print "-------------------------"
    #
    # labelsAndPreds.foreach(printR)

    sc.stop()
    print("Training Error = " + str(trainErr))