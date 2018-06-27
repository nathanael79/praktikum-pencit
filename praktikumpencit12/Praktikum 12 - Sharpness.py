import imageio
import matplotlib.pyplot as plt
import numpy as np

imgNormal = imageio.imread("lamb.jpg")

imgGrayscale = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(0, imgNormal.shape[0]):
    for x in range(0, imgNormal.shape[1]):
        r = imgNormal[y][x][0]
        g = imgNormal[y][x][1]
        b = imgNormal[y][x][2]
        gr = ( int(r) + int(g) + int(b) ) / 3
        imgGrayscale[y][x] = (gr, gr, gr)


imgSharpnessGray = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(1, imgNormal.shape[0] - 1):
    for x in range(1, imgNormal.shape[1] - 1):
        x1 = int(imgGrayscale[y - 1][x - 1][0])
        x2 = int(imgGrayscale[y][x - 1][0])
        x3 = int(imgGrayscale[y + 1][x - 1][0])
        x4 = int(imgGrayscale[y - 1][x][0])
        x5 = int(imgGrayscale[y][x][0])
        x6 = int(imgGrayscale[y + 1][x][0])
        x7 = int(imgGrayscale[y - 1][x + 1][0])
        x8 = int(imgGrayscale[y][x + 1][0])
        x9 = int(imgGrayscale[y + 1][x + 1][0])
        xt1 = int((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) / 9)
        xt2 = int(-x1 - (2 * x2) - x3 + x7 + (2 * x8) + x9)
        xt3 = int(-x1 - (2 * x4) - x7 + x3 + (2 * x6) + x9)
        xb = int(xt1 + xt2 + xt3)
        if xb < 0:
            xb = -xb
        if xb > 255:
            xb = 255
        imgSharpnessGray[y][x] = (xb, xb, xb)
        
plt.imshow(imgSharpnessGray)
plt.title("Sharpness Gray")
plt.show()


# ## Sharpness Gray (2:1 LPF:HPF)


imgSharpnessGrayL = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(1, imgNormal.shape[0] - 1):
    for x in range(1, imgNormal.shape[1] - 1):
        x1 = int(imgGrayscale[y - 1][x - 1][0])
        x2 = int(imgGrayscale[y][x - 1][0])
        x3 = int(imgGrayscale[y + 1][x - 1][0])
        x4 = int(imgGrayscale[y - 1][x][0])
        x5 = int(imgGrayscale[y][x][0])
        x6 = int(imgGrayscale[y + 1][x][0])
        x7 = int(imgGrayscale[y - 1][x + 1][0])
        x8 = int(imgGrayscale[y][x + 1][0])
        x9 = int(imgGrayscale[y + 1][x + 1][0])
        xt1 = int((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) / 9)
        xt2 = int(-x1 - (2 * x2) - x3 + x7 + (2 * x8) + x9)
        xt3 = int(-x1 - (2 * x4) - x7 + x3 + (2 * x6) + x9)
        xb = int((2 * xt1) + xt2 + xt3)
        if xb < 0:
            xb = -xb
        if xb > 255:
            xb = 255
        imgSharpnessGrayL[y][x] = (xb, xb, xb)
        
plt.imshow(imgSharpnessGrayL)
plt.title("Sharpness Gray 2:1")
plt.show()


# ## Sharpness Gray (1:2 LPF:HPF)

imgSharpnessGrayH = np.zeros((imgNormal.shape[0], imgNormal.shape[1], 3), dtype=np.uint8)

for y in range(1, imgNormal.shape[0] - 1):
    for x in range(1, imgNormal.shape[1] - 1):
        x1 = int(imgGrayscale[y - 1][x - 1][0])
        x2 = int(imgGrayscale[y][x - 1][0])
        x3 = int(imgGrayscale[y + 1][x - 1][0])
        x4 = int(imgGrayscale[y - 1][x][0])
        x5 = int(imgGrayscale[y][x][0])
        x6 = int(imgGrayscale[y + 1][x][0])
        x7 = int(imgGrayscale[y - 1][x + 1][0])
        x8 = int(imgGrayscale[y][x + 1][0])
        x9 = int(imgGrayscale[y + 1][x + 1][0])
        xt1 = int((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) / 9)
        xt2 = int(-x1 - (2 * x2) - x3 + x7 + (2 * x8) + x9)
        xt3 = int(-x1 - (2 * x4) - x7 + x3 + (2 * x6) + x9)
        xb = int(xt1 + (2 * xt2) + (2 * xt3))
        if xb < 0:
            xb = -xb
        if xb > 255:
            xb = 255
        imgSharpnessGrayH[y][x] = (xb, xb, xb)
        
plt.imshow(imgSharpnessGrayH)
plt.title("Sharpness Gray 1:2")
plt.show()
