#coding=utf-8
from PIL import Image
import numpy
from numpy import linalg as lg

imagePath = '/Users/yinchuandong/Pictures/study1.png'


def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i, k]) > thresh:
                print 1,
            else:
                print 0,
        print ''


def imgCompress(numSV=3, thresh=0.8):
    myl = []
    for line in open('0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = numpy.mat(myl)
    print "****original matrix******"
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)
    SigRecon = numpy.mat(zeros((numSV, numSV)))
    for k in range(numSV):  # construct diagonal matrix from vector
        SigRecon[k, k] = Sigma[k]
    reconMat = U[:, :numSV] * SigRecon * VT[:numSV, :]
    print "****reconstructed matrix using %d singular values******" % numSV
    printMat(reconMat, thresh)


def run():
    numSV = 480 #奇异矩阵的个数
    im = Image.open(imagePath)
    imgArr = numpy.array(im)
   

    finalArr = numpy.empty(imgArr.shape, dtype=numpy.uint8)
    # print finalArr

    channelCount = imgArr.shape[2]
    for channelNum in range(channelCount):
        matrix = imgArr[:,:,channelNum]
        U, Sigma, VT = lg.svd(matrix)
        SigRecon = numpy.mat(numpy.zeros((numSV, numSV)))
        for k in range(numSV):
            SigRecon[k, k] = Sigma[k]
        reconMat = U[:, :numSV] * SigRecon * VT[:numSV, :]
        finalArr[:, :, channelNum] = reconMat
    
    # print finalArr  
    im2 = Image.fromarray(finalArr)
    print imgArr.shape   
    # im2.show()
    im2.save('test.png')
    
    return

if __name__ == '__main__':
    print 'main function'
    run()
