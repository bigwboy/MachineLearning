# -*- coding: utf8 -*-
#time:2017/9/19 11:34
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
from numpy import *

# load data 导入数据
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fd = open(fileName)
    for line in fd.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

# linear regression 计算回归系数
def linearRegres(xVec, yVec):
    xMat = mat(xVec);yMat = mat(yVec).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0:        # 奇异矩阵不能求逆
        print('This matrix is singular, cannot do inverse')
        return
    theta = xTx.I * xMat.T * yMat
    return theta

#DEBUG
if __name__ == "__main__":
	pass