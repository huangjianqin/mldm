# -*- coding:utf-8 -*-
from pyspark import SparkConf, SparkContext
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.util import MLUtils

if __name__ == "__main__":
    # Load and parse the data file into an RDD of LabeledPoint.
    conf = SparkConf().setAppName("DecisionTreeForClassifier").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    data = MLUtils.loadLibSVMFile(sc, '../sample_multiclass_classification_data.txt')
    # Split the data into training and test sets (30% held out for testing)
    (trainingData, testData) = data.randomSplit([0.7, 0.3])

    # Train a DecisionTree model.
    #  Empty categoricalFeaturesInfo indicates all features are continuous.
    # entropy / gini
    model = DecisionTree.trainClassifier(trainingData, numClasses=3, categoricalFeaturesInfo={},
                                         impurity='entropy')

    # Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
    testErr = labelsAndPredictions.filter(lambda (v, p): v != p).count() / float(testData.count())
    print('Test Error = ' + str(testErr))
    print('Learned classification tree model:')
    print(model.toDebugString())