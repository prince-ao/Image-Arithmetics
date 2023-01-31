import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pylab as plt

im1 = mpimg.imread("./images/shelf.jpg")
im2 = mpimg.imread("./images/painting.jpg")

subtraction = im1 - im2
subtraction[subtraction < 0] = 0

subtraction = Image.fromarray(subtraction)
subtraction.save("./images/shelf-minus-painting.jpg")
