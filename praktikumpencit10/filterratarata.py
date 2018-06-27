import imageio
import matplotlib.pyplot as plt
import numpy as np
import random

imgNormal = imageio.imread("lamb.jpg")
#plt.imshow(imgNormal)
#plt.title("Showing image")
#plt.show()
imgGrayScale = np.zeros((imgNormal.shape[0], imgNormal.shape[1],3),dtype=np.uint8)
for y in range(0, imgNormal.shape[0]):
    for x in range (0, imgNormal.shape[1]):
        r = imgNormal[y][x][0]
        g = imgNormal[y][x][1]
        b = imgNormal[y][x][2]
        gr = (int(r)+int(g)+int(b))/3
        imgGrayScale[y][x] = (gr,gr,gr)

imgNoiseGaussian = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)
imgNoiseSaltPepper = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)
imgNoiseSpeckle = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)

imgFilterRataGaus = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)
imgFilterRataSpeckle = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)
imgFilterRataSaltPepper = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)

#menambahkan noise gaussian
'''for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayScale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr<20:
            ns = random.randint(0,256) - 128
            xb = int(xg+ns)
            if xb < 0 :
                xb = -xb
            if xb > 255:
                xb = 255
        imgNoiseGaussian[y][x] = (xb,xb,xb)

#menambahkan noise

for y in range (0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayScale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr<20:
            xb = 255
        imgNoiseSaltPepper[y][x] = (xb,xb,xb)

#menambahkan Speckle Noise

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayScale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr<20:
            xb = 0
        imgNoiseSpeckle[y][x]=(xb,xb,xb)

'''
for y in range(1, imgNormal.shape[0] - 1):
    for x in range(1, imgNormal.shape[1] - 1):
        #noise gaussian
        x1 = int(imgNoiseGaussian[y-1][x-1][0])
        x2 = int(imgNoiseGaussian[y][x-1][0])
        x3 = int(imgNoiseGaussian[y+1][x - 1][0])
        x4 = int(imgNoiseGaussian[y-1][x][0])
        x5 = int(imgNoiseGaussian[y][x][0])
        x6 = int(imgNoiseGaussian[y+1][x][0])
        x7 = int(imgNoiseGaussian[y-1][x+1][0])
        x8 = int(imgNoiseGaussian[y][x+1][0])
        x9 = int(imgNoiseGaussian[y+1][x+1][0])
        xb = int((x1+x2+x3+x4+x5+x6+x7+x8+x9)/ 9)
        if xb < 0 :
            xb = 0
        if xb > 255 :
            xb = 255
        imgFilterRataGaus[y][x] = (xb,xb,xb)

        #noise speckle
        x1 = int(imgNoiseSpeckle[y-1][x-1][0])
        x2 = int(imgNoiseSpeckle[y][x-1][0])
        x3 = int(imgNoiseSpeckle[y+1][x - 1][0])
        x4 = int(imgNoiseSpeckle[y-1][x][0])
        x5 = int(imgNoiseSpeckle[y][x][0])
        x6 = int(imgNoiseSpeckle[y+1][x][0])
        x7 = int(imgNoiseSpeckle[y-1][x+1][0])
        x8 = int(imgNoiseSpeckle[y][x+1][0])
        x9 = int(imgNoiseSpeckle[y+1][x+1][0])
        xb = int((x1+x2+x3+x4+x5+x6+x7+x8+x9)/ 9)
        if xb < 0 :
            xb = 0
        if xb > 255 :
            xb = 255
        imgFilterRataSpeckle[y][x] = (xb,xb,xb)
        #Noise Salt & Pepper
        x1 = int(imgNoiseSaltPepper[y - 1][x - 1][0])
        x2 = int(imgNoiseSaltPepper[y][x - 1][0])
        x3 = int(imgNoiseSaltPepper[y + 1][x - 1][0])
        x4 = int(imgNoiseSaltPepper[y - 1][x][0])
        x5 = int(imgNoiseSaltPepper[y][x][0])
        x6 = int(imgNoiseSaltPepper[y + 1][x][0])
        x7 = int(imgNoiseSaltPepper[y - 1][x + 1][0])
        x8 = int(imgNoiseSaltPepper[y][x + 1][0])
        x9 = int(imgNoiseSaltPepper[y + 1][x + 1][0])
        xb = int((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) / 9)
        if xb < 0 :
            xb = 0
        if xb > 255 :
            xb = 255
        imgFilterRataSaltPepper[y][x]=(xb,xb,xb)

        plt.imshow(imgFilterRataGaus)
        plt.title("Filter Rata Rata | Noise Gaussian")
        plt.show()


