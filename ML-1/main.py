# Kangjier@2021:FocalAcoustics.CODE.The maintenance email is Jwjier@gmail.com .


def loadDataSet():
    '''
    加载数据集 :return 向量矩阵 / 向量
    '''
    dataMat = []; labelMat = []

    fr = open('/Users/Jier/JobCode/ML-code/ML-1/data/TSet.txt')
    for l in fr.readlines():
        lineArr = l.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def plotBestFit(weights):
    '''
    画出数据集和逻辑斯蒂最佳回归直线
    '''
    import matplotlib.pyplot as plt
    import numpy as np


    dataMat,labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []

    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    if weights is not None:
        x = arange(-3.0, 3.0, 0.1)
        y = (-weights[0]-weights[1]*x)/weights[2]  
        ax.plot(x, y)                             
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
plotBestFit(None)