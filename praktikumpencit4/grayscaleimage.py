import numpy as np
import imageio
import matplotlib.pyplot as plt

img =  imageio.imread("surabayapy.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = 3
img_type = img.dtype

img_gray = np.zeros((img_height, img_width,3), dtype=np.uint8)

for y in range (0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img [y][x][2]
        gray = (int(red)+int(green)+int(blue))/3
        img_gray[y][x] = (gray, gray, gray)

plt.imshow(img_gray)
plt.title("Grayscale Image")
plt.show()