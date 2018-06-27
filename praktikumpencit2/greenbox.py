import numpy as np
import matplotlib.pyplot as plt
import imageio

img_green = np.zeros((256,256,3), dtype=np.uint8)
for y in range(0, 256):
    for x in range(0, 256):
        for c in range(0,3):
            if c ==1:
                img_green[y][x][c] = 255
            else:
                img_green[y][x][c] = 0


plt.imshow(img_green)
plt.title("Green Box")
plt.show()