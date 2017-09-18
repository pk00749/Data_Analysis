# -*- coding:utf-8 -*-
import csv
from numpy import *
import operator
import KNN


def load_train_data():
    raw_data = []
    with open('train.csv') as train_file:
        lines = csv.reader(train_file)
        for line in lines:
            raw_data.append(line)

    raw_data.remove(raw_data[0])
    raw_data = array(raw_data)
    data = raw_data[:, 1:]
    label = raw_data[:, 0]
    print label
    print "train data loaded"
    return normalizing(tolnt(data)), tolnt(label)


def tolnt(array):
    array = mat(array)
    row, col = shape(array)
    new_array = zeros((row, col))
    for r in xrange(row):
        for c in xrange(col):
            new_array[r, c] = int(array[r, c])
    return new_array


def normalizing(array):
    row, col = shape(array)
    for r in xrange(row):
        for c in xrange(col):
            if array[r, c] != 0:
                array[r, c] = 1
    return array


def load_test_data():
    test_data = []
    with open('test.csv') as test_file:
        lines = csv.reader(test_file)
        for line in lines:
            test_data.append(line)

    test_data.remove(test_data[0])  # (28000, 784)
    test_data = array(test_data)
    print "Test data loaded"
    return normalizing(tolnt(test_data))


def classify_knn(inX, dataset, label, k):
    inX = mat(inX)
    dataSet = mat(dataset)
    labels = mat(label)  # (42000, 1)
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = array(diffMat)**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i], 0]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "Classified"
    return sortedClassCount[0][0]


def save_result(result):
    with open('result.csv', 'wb') as myFile:
        myWriter = csv.writer(myFile)
        for i in result:
            tmp=[]
            tmp.append(i)
            myWriter.writerow(tmp)
    print "Saved"


def handwritingClassTest():
    trainData, trainLabel = load_train_data()
    testData = load_test_data()

    m, n = shape(testData)
    resultList=[]
    for i in range(m):
        classiferResult = classify_knn(testData[i], trainData, trainLabel.transpose(), 5)
        resultList.append(classiferResult)
        print "The classifier came back with: %d" % (classiferResult)
    save_result(resultList)


if __name__ == '__main__':
    handwritingClassTest()
    print 'ok'

