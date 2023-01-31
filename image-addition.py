import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pylab as plt

im1 = mpimg.imread("./images/shelf.jpg")
im2 = mpimg.imread("./images/painting.jpg")

addition = im1 + im2
addition[addition > 255] = 255

addition = Image.fromarray(addition)
addition.save("./images/shelf-plus-painting.jpg")
