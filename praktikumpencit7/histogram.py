import numpy as np
import matplotlib.pyplot as plt
import imageio

img = imageio.imread("android.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_grayscale = np.zeros((img_height,img_width,3), dtype=np.uint8)
for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue)) / 3
        img_grayscale[y][x] = (gray, gray, gray)

hg = np.zeros((256))
for x in range(0, 256):
    hg[x]=0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray]+=1

bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()