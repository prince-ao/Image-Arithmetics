import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pylab as plt

im1 = mpimg.imread("./images/outlet.jpg")
im2 = mpimg.imread("./images/windows.jpg")

im1_t = Image.fromarray(im1)
im1_t = im1_t.convert('L') # convert to gray scale
im1_t.save("./images/outlet-gray.jpg")
im1 = np.array(im1_t)

im2_t = Image.fromarray(im2)
im2_t = im2_t.convert('L') # convert to gray scale
im2_t.save("./images/windows-gray.jpg")
im2 = np.array(im2_t)

division = np.ndarray(im1.shape)

for i in range(im1.shape[0]):
    for j in range(im1.shape[1]):
        division[i][j] = im1[i][j] / (im2[i][j] if im2[i][j] != 0 else 1)

division = division.astype(np.uint8)
division = Image.fromarray(division)
division.convert("L")
division.save("./images/outlet-divide-windows-gray.jpg")