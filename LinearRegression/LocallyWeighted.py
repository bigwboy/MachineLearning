# -*- coding: utf8 -*-
#time:2017/9/18 14:25
#VERSION:1.0
#__OUTHOR__:guangguang
#Email:kevinliu830829@163.com
from numpy import *


def standRegres(xArr,yArr):
    xMat = mat(xArr)

    #转置
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print 'This matrix is singular, cannot do inverse'
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws



def plotStandRegres(xArr,yArr,ws):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([i[1] for i in xArr],yArr,'ro')
    xCopy = xArr
    print type(xCopy)
    xCopy.sort()
    yHat = xCopy*ws
    ax.plot([i[1] for i in xCopy],yHat)
    plt.show()

def calcCorrcoef(xArr,yArr,ws):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat*ws
    return corrcoef(yHat.T, yMat)

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):
        #计算权重
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))

    #奇异矩阵不计算
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return

    #回归系数
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

#多所有点进行计算
def lwlrTest(testArr,xArr,yArr,k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def lwlrTestPlot(xArr,yArr,k=1.0):
    import matplotlib.pyplot as plt
    yHat = zeros(shape(yArr))
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([i[1] for i in xArr],yArr,'ro')
    ax.plot(xCopy,yHat)
    plt.show()
    #return yHat,xCopy

def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()


#数据输入
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat


#DEBUG
if __name__ == "__main__":
    #数据输入
    DATA=sys.argv[1]
    xArr, yArr = loadDataSet(DATA)

    #数据转置
    ws = standRegres(xArr, yArr)
    print ws

    # plotStandRegres(xArr,yArr,ws)
    print calcCorrcoef(xArr, yArr, ws)
    # lwlr
    lwlrTestPlot(xArr, yArr, k=1)