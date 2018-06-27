import numpy as np
import matplotlib.pyplot as plt
import imageio

img = imageio.imread("ubuntu.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

plt.imshow(img)
plt.title("Load an Image")
plt.show()