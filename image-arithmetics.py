import numpy as np
from PIL import Image
from math import log as mathlog, sqrt as mathsqrt

class ImageArithmetics:
    def __init__(self, image_path):
        im = Image.open(image_path)
        im = im.convert('L')
        self.image = np.array(im)
        self.path = image_path.split(".")
        

    def add(self, C):
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] += C
        image[image > 255] = 255
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_add.{self.path[-1]}")

    def subtract(self, C):
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] -= C
        image[image < 0] = 0
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_sub.{self.path[-1]}")

    def multiply(self, C):
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] *= C
        image[image > 255] = 255
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_mult.{self.path[-1]}")

    def divide(self, C):
        if C == 0:
            raise ValueError("C != 0")
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] /= C
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_div.{self.path[-1]}")

    def log(self):
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] = mathlog(image[i, j] if image[i, j] != 0 else 1)
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_log.{self.path[-1]}")

    def sqrt(self):
        image = np.copy(self.image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] = mathsqrt(image[i, j])
        im = Image.fromarray(image)
        im.save(f"{self.path[0]}_sqrt.{self.path[-1]}")


i = ImageArithmetics("images/ciel.jpg")
i.log()
i.sqrt()