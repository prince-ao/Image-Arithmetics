import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pylab as plt

def add(img1, img2, out):
    im1 = mpimg.imread(img1)
    im2 = mpimg.imread(img2)

    addition = im1 + im2
    addition[addition > 255] = 255

    addition = Image.fromarray(addition)
    addition.save(out)

add("./images/shelf.jpg", "./images/painting.jpg", "./images/shelf-plus-painting.jpg")