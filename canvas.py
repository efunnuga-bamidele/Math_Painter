import numpy as np
from PIL import Image
import os


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        self.imagepath = imagepath
        os.chdir("images")
        self.img = Image.fromarray(self.data, 'RGB')
        self.img.save(imagepath)
