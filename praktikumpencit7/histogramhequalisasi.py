import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread("android.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_grayscale = np.zeros((img_height,img_width,3), dtype=np.uint8)

hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1

h[0] = hgh[0]
for x in range(1, 256):
    h[x] = h[x - 1] + hgh[x]

for x in range(0, 256):
    h[x] = h[x] / img_height / img_width

for x in range(0, 256):
    hgh[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0]
for x in range(1, 256):
    c[x] = c[x - 1] + hgh[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

bins = np.linspace(0, 256, 100)
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()