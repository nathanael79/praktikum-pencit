import imageio
import matplotlib.pyplot as plt
import numpy as np


imgNormal = imageio.imread("lamb.jpg")

imgBrightness = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
a = 100 # -100 ~ 100
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = int(imgNormal[y][x][0]) + a
        g = int(imgNormal[y][x][1]) + a
        b = int(imgNormal[y][x][2]) + a
        if r < 0:
            r = 0
        if r > 255:
            r = 255
        if g < 0:
            g = 0
        if g > 255:
            g = 255
        if b < 0:
            b = 0
        if b > 255:
            b = 255
        imgBrightness[y][x] = (r, g, b)

plt.imshow(imgBrightness)
plt.title("Image Brightness (+" + str(a) + ")")
plt.show()

imgContrass = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
c = 150 # 10 ~ 200
c = float(c/100)
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = int(float(imgNormal[y][x][0]) * c)
        g = int(float(imgNormal[y][x][1]) * c)
        b = int(float(imgNormal[y][x][2]) * c)
        if r < 0:
            r = 0
        if r > 255:
            r = 255
        if g < 0:
            g = 0
        if g > 255:
            g = 255
        if b < 0:
            b = 0
        if b > 255:
            b = 255
        imgContrass[y][x] = (r, g, b)

plt.imshow(imgContrass)
plt.title("Image Contrass (+" + str(c) + ")")
plt.show()


# ## Invers


imgInvers = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = 255 - int(imgNormal[y][x][0])
        g = 255 - int(imgNormal[y][x][1])
        b = 255 - int(imgNormal[y][x][2])
        imgInvers[y][x] = (r, g, b)

plt.imshow(imgInvers)
plt.title("Image Invers")
plt.show()


# ## Auto Level


imgAutoLevel = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)
rmin = 255
gmin = 255
bmin = 255
rmax = 0
gmax = 0
bmax = 0

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = int(imgNormal[y][x][0])
        g = int(imgNormal[y][x][1])
        b = int(imgNormal[y][x][2])
        if r < rmin:
            rmin = r
        if r > rmax:
            rmax = r
        if g < gmin:
            gmin = g
        if g > gmax:
            gmax = g
        if b < bmin:
            bmin = b
        if b > bmax:
            bmax = b

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = int(imgNormal[y][x][0])
        g = int(imgNormal[y][x][1])
        b = int(imgNormal[y][x][2])
        rbaru = int(255 * (r - rmin) / (rmax - rmin))
        gbaru = int(255 * (g - gmin) / (gmax - gmin))
        bbaru = int(255 * (b - bmin) / (bmax - bmin))
        imgAutoLevel[y][x] = (rbaru, gbaru, bbaru)

plt.imshow(imgAutoLevel)
plt.title("Image Auto Level")
plt.show()


# ## Kuantisasi

imgKuantisasiRGB = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

th = int(256/4)
for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        red = int(imgNormal[y][x][0])
        green = int(imgNormal[y][x][1])
        blue = int(imgNormal[y][x][2])
        red = th * int(red/th)
        green = th * int(green/th)
        blue = th * int(blue/th)
        imgKuantisasiRGB[y][x] = (red, green, blue)

plt.imshow(imgKuantisasiRGB)
plt.title("Image Kuantisasi 4")
plt.show()

