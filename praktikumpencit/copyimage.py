import numpy as np
import matplotlib.pyplot as plt
import imageio

img = imageio.imread("ubuntu.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_copy = np.zeros(img.shape, img.dtype)

for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_copy[y][x][c]=img[y][x][c]

plt.imshow(img_copy)
plt.title("Copy an Image")
plt.imsave("saved-copy-nuel.jpg",img_copy)
plt.show()