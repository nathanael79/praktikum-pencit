import numpy as np
import matplotlib.pyplot as plt
import imageio

img_indonesia_flag = np.zeros((640,1280,3), dtype=np.uint8)

for y in range(0, 640):
    for x in range(0, 1280):
        for c in range(0,3):
            if y >=320:
                img_indonesia_flag[y][x][c] = 255
            else:
                if c == 0:
                    img_indonesia_flag[y][x][c] = 255
                else:
                    img_indonesia_flag[y][x][c]=0


plt.imshow(img_indonesia_flag)
plt.title("Bendera Indonesia")
plt.show()