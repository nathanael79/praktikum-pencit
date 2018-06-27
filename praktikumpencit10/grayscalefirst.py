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

plt.imshow(imgGrayScale)
plt.title("Grayscale Image")
plt.show()