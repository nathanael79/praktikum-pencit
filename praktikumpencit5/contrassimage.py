import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread("youtube.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

img_contrass = np.zeros(img.shape, dtype=np.uint8)

def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray *= nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)

contrass(2)
plt.imshow(img_contrass)
plt.title("Using Contrass 2 to the Image")
plt.show()

contrass(3)
plt.imshow(img_contrass)
plt.title("Using Contrass 3 to the Image")
plt.show()