import imageio
import numpy as np
import matplotlib.pyplot as plt

img = imageio.imread("android.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_nthpower = np.zeros((img_height, img_width, 3), dtype=np.uint8)

def nthpower(c, y):
    thc = c / 100
    thy = c / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue))/3
            gray = int(thc*pow(gray,thy))
            if gray > 255 :
                gray = 255
            if gray < 0 :
                gray = 0
            img_nthpower[y][x]=(gray, gray, gray)

nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("image using nthpower")
plt.show()