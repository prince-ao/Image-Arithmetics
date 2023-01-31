import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pylab as plt

im1 = mpimg.imread("./images/outlet.jpg")
im2 = mpimg.imread("./images/windows.jpg")

multiplication = im1 * im2
multiplication[multiplication > 255] = 255

multiplication = Image.fromarray(multiplication)
multiplication.save("./images/outlet-times-windows.jpg")
