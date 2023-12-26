import sys
import numpy as np
import operator
from os import listdir

def createDataSet(dirName):
    labels = []
    trainingFileList = listdir(dirName)
    length = len(trainingFileList)
    matrix = np.zeros((length, 1024)) 
    for i in range(length): 
        fileName = trainingFileList[i]
        num = int(fileName.split('_')[0])  
        labels.append(num)
        matrix[i, :] = autoNorm(dirName + '/' + fileName)
    return matrix, labels 

def autoNorm(fileName):  
    normDataSet = np.zeros((1, 1024)) 
    with open(fileName) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                normDataSet[0, 32 * i + j] = int(line[j])
        return normDataSet        

def classify0(inX, dataSet, labels, k): 
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis = 1) 
    distances = sqDistances ** 0.5 
    sortedDistIndicies = distances.argsort() 
    classCount = {} 
    for i in range(k): 
        voteIlabel = labels[sortedDistIndicies[i]]  
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True) 
    return sortedClassCount[0][0]

trainingFileName = sys.argv[1]
testFileName = sys.argv[2]
testFileList = listdir(testFileName)
length = len(testFileList)
matrix, labels = createDataSet(trainingFileName)

for k in range(1, 21): 
    cnt = 0 
    errorCnt = 0 
    for i in range(length): 
        num = int(testFileList[i].split('_')[0])
        testData = autoNorm(testFileName + '/' + testFileList[i])
        result = classify0(testData, matrix, labels, k)
        cnt += 1
        if num != result:
            errorCnt += 1
    print(int(errorCnt / cnt * 100))
