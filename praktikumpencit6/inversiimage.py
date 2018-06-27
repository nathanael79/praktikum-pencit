import imageio
import numpy as np
import matplotlib.pyplot as plt

img = imageio.imread("android.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_inversi = np.zeros((img_height, img_width, 3), dtype=np.uint8)

def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range (0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue))/3
            gray = nilai - gray
            img_inversi[y][x] = (gray, gray, gray)

def inversi_rgb(nilai):
    for y in range (0, img_height):
        for x in range (0, img_width):
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            green = nilai - green
            blue = img[y][x][2]
            blue = nilai - blue
            img_inversi[y][x] = (red, green, blue)

inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inverse an Image")
plt.show()

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inverse an Image using RGB")
plt.show()