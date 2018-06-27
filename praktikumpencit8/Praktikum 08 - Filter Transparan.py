
# coding: utf-8

# # Praktikum 8 | Pengolahan Citra

# ## Filter Transparan

# Fadhil Yori Hibatullah | 2103161037 | 2 D3 Teknik Informatika B

# ----------------------------

# ### Import Library

# In[1]:


import numpy as np
import imageio
import matplotlib.pyplot as plt


# ### Membaca Gambar

# In[2]:


img1 = imageio.imread("gambar1.png") # dasar
img2 = imageio.imread("gambar2.png")

plt.imshow(img1)
plt.title("Gambar 1")
plt.show()

plt.imshow(img2)
plt.title("Gambar 2")
plt.show()


# In[3]:


img_height = img1.shape[0]
img_width = img1.shape[1]
img_channel = img1.shape[2]

if img1.shape[0] > img2.shape[0]:
    height = img1.shape[0]
else:
    height = img2.shape[0]
    
if img1.shape[1] > img2.shape[1]:
    width = img1.shape[1]
else:
    width = img2.shape[1]
    
imshape = (height, width, 3)
print(imshape)


# -----------------------------

# ## Menggabungkan kedua gambar, dengan img1 merupakan bagian dasar

# In[4]:


img_trans = np.zeros(imshape, dtype=np.uint8)

for y in range(0, height):
    for x in range(0, width):
        try:
            r1 = img1[y][x][0]
            g1 = img1[y][x][1]
            b1 = img1[y][x][2]
        except:
            r1 = 0
            g1 = 0
            b1 = 0
        try:
            r2 = img2[y][x][0]
            g2 = img2[y][x][1]
            b2 = img2[y][x][2]
        except:
            r2 = 0
            g2 = 0
            b2 = 0
        r = (0.5 * r1) + (0.5 * r2)
        g = (0.5 * g1) + (0.5 * g2)
        b = (0.5 * b1) + (0.5 * b2)
        img_trans[y][x] = (r,g,b)


# In[5]:


plt.imshow(img_trans)
plt.title("Done")
plt.show()

