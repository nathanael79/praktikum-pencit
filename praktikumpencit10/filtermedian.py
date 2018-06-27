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

imgFilterMedianGaussian = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
imgFilterMedianSpeckle = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
imgFilterMedianSaltPepper = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
xt = np.zeros((10))
for y in range(1, imgNormal.shape[0] - 1):
    for x in range(1, imgNormal.shape[1] - 1):
        # Noise Gaussian
        xt[1] = int(imgNoiseGaussian[y - 1][x - 1][0])
        xt[2] = int(imgNoiseGaussian[y][x - 1][0])
        xt[3] = int(imgNoiseGaussian[y + 1][x - 1][0])
        xt[4] = int(imgNoiseGaussian[y - 1][x][0])
        xt[5] = int(imgNoiseGaussian[y][x][0])
        xt[6] = int(imgNoiseGaussian[y + 1][x][0])
        xt[7] = int(imgNoiseGaussian[y - 1][x + 1][0])
        xt[8] = int(imgNoiseGaussian[y][x + 1][0])
        xt[9] = int(imgNoiseGaussian[y + 1][x + 1][0])
        for i in range(1, 9):
            for j in range(1, 9):
                if xt[j] > xt[j + 1]:
                    a = xt[j]
                    xt[j] = xt[j + 1]
                    xt[j + 1] = a
        xb = xt[5]
        imgFilterMedianGaussian[y][x] = (xb, xb, xb)
        # Noise Speckle
        xt[1] = int(imgNoiseSpeckle[y - 1][x - 1][0])
        xt[2] = int(imgNoiseSpeckle[y][x - 1][0])
        xt[3] = int(imgNoiseSpeckle[y + 1][x - 1][0])
        xt[4] = int(imgNoiseSpeckle[y - 1][x][0])
        xt[5] = int(imgNoiseSpeckle[y][x][0])
        xt[6] = int(imgNoiseSpeckle[y + 1][x][0])
        xt[7] = int(imgNoiseSpeckle[y - 1][x + 1][0])
        xt[8] = int(imgNoiseSpeckle[y][x + 1][0])
        xt[9] = int(imgNoiseSpeckle[y + 1][x + 1][0])
        for i in range(1, 9):
            for j in range(1, 9):
                if xt[j] > xt[j + 1]:
                    a = xt[j]
                    xt[j] = xt[j + 1]
                    xt[j + 1] = a
        xb = xt[5]
        imgFilterMedianSpeckle[y][x] = (xb, xb, xb)
        # Noise Salt and Pepper
        xt[1] = int(imgNoiseSaltPepper[y - 1][x - 1][0])
        xt[2] = int(imgNoiseSaltPepper[y][x - 1][0])
        xt[3] = int(imgNoiseSaltPepper[y + 1][x - 1][0])
        xt[4] = int(imgNoiseSaltPepper[y - 1][x][0])
        xt[5] = int(imgNoiseSaltPepper[y][x][0])
        xt[6] = int(imgNoiseSaltPepper[y + 1][x][0])
        xt[7] = int(imgNoiseSaltPepper[y - 1][x + 1][0])
        xt[8] = int(imgNoiseSaltPepper[y][x + 1][0])
        xt[9] = int(imgNoiseSaltPepper[y + 1][x + 1][0])
        for i in range(1, 9):
            for j in range(1, 9):
                if xt[j] > xt[j + 1]:
                    a = xt[j]
                    xt[j] = xt[j + 1]
                    xt[j + 1] = a
        xb = xt[5]
        imgFilterMedianSaltPepper[y][x] = (xb, xb, xb)

plt.imshow(imgFilterMedianGaussian)
plt.title("Filter Median | Noise Gaussian")
plt.show()

plt.imshow(imgFilterMedianSpeckle)
plt.title("Filter Median | Noise Speckle")
plt.show()

plt.imshow(imgFilterMedianSaltPepper)
plt.title("Filter Median | Noise Salt and Pepper")
plt.show()