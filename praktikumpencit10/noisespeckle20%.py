import imageio
import matplotlib.pyplot as plt
import numpy as np
import random

imgNormal = imageio.imread("lamb.jpg")
imgNoiseGaussian = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)
imgGrayScale = np.zeros((imgNormal.shape[0], imgNormal.shape[1],3),dtype=np.uint8)
for y in range(0, imgNormal.shape[0]):
    for x in range (0, imgNormal.shape[1]):
        r = imgNormal[y][x][0]
        g = imgNormal[y][x][1]
        b = imgNormal[y][x][2]
        gr = (int(r)+int(g)+int(b))/3
        imgGrayScale[y][x] = (gr,gr,gr)

imgNoiseSpeckle = np.zeros((imgNormal.shape[0],imgNormal.shape[1],3),dtype=np.uint8)

#menambahkan Speckle Noise

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayScale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr<20:
            xb = 0
        imgNoiseSpeckle[y][x]=(xb,xb,xb)

plt.imshow(imgNoiseSpeckle)
plt.title("Noise Speckle 20%")
plt.show()