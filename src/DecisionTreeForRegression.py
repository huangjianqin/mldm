# -*- coding:utf-8 -*-
from pyspark import SparkConf, SparkContext
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.util import MLUtils

if __name__ == "__main__":
    conf = SparkConf().setAppName("DecisionTreeForRegression").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    # Load and parse the data file into an RDD of LabeledPoint.
    data = MLUtils.loadLibSVMFile(sc, '../sample_libsvm_data.txt')
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a DecisionTree model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    model = DecisionTree.trainRegressor(trainingData, categoricalFeaturesInfo={},
                                        impurity='variance', maxDepth=5, maxBins=32)

    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testMSE = labelsAndPredictions.map(lambda (v, p): (v - p) * (v - p)).sum() / \
              float(testData.count())
    print('Test Mean Squared Error = ' + str(testMSE))
    print('Learned regression tree model:')
    print(model.toDebugString())