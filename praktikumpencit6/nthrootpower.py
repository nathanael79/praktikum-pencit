import imageio
import numpy as np
import matplotlib.pyplot as plt

img = imageio.imread("android.png")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

img_nthrootpower = np.zeros((img_height, img_width,3), dtype=np.uint8)

def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthrootpower[y][x] = (gray, gray, gray)

nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()