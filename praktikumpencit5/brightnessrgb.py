import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread("youtube.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

img_rgbbrightness = np.zeros(img.shape, dtype=np.uint8)

def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbrightness[y][x] = (red, green, blue)

rgbbrighter(-100)
plt.imshow(img_rgbbrightness)
plt.title("Using Brightness -100 to the image")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbrightness)
plt.title("Using Brightness 100 to the image")
plt.show()