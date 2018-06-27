import numpy as np
import matplotlib.pyplot as plt
import imageio

img =  imageio.imread("surabayapy.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = 3
img_type = img.dtype

img_biner = np.zeros((img_height, img_width,3), dtype=np.uint8)

for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        gray = (int(red) + int(green) + int(blue))/3
        if gray < 128:
            gray = 0
        else :
            gray = 255
            img_biner [y][x] = (gray, gray, gray)

plt.imshow(img_biner)
plt.title("Biner Image")
plt.show()