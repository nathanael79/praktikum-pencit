import imageio
import matplotlib.pyplot as plt
import numpy as np
import random
import cv2

imgNormal = imageio.imread("lamb.jpg")


imgGrayscale = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = imgNormal[y][x][0]
        g = imgNormal[y][x][1]
        b = imgNormal[y][x][2]
        gr = ( int(r) + int(g) + int(b) ) / 3
        imgGrayscale[y][x] = (gr, gr, gr)

imgNoiseGaussian = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

# Add noise
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayscale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr < 20:
            ns = random.randint(0,256) - 128
            xb = int(xg + ns)
            if xb < 0:
                xb = -xb
            if xb > 255:
                xb = 255
        imgNoiseGaussian[y][x] = (xb, xb, xb)

plt.imshow(imgNoiseGaussian)
plt.title("Noise Gaussian")
plt.show()

imgNoiseSpeckle = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

# Add noise
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayscale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr < 20:
            xb = 0
        imgNoiseSpeckle[y][x] = (xb, xb, xb)

plt.imshow(imgNoiseSpeckle)
plt.title("Noise Speckle")
plt.show()

imgNoiseSaltPepper = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

# Add noise
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        xg = imgGrayscale[y][x][0]
        xb = xg
        nr = random.randint(0,100)
        if nr < 20:
            xb = 255
        imgNoiseSaltPepper[y][x] = (xb, xb, xb)

plt.imshow(imgNoiseSaltPepper)
plt.title("Noise Salt and Pepper")
plt.show()





