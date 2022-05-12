import numpy as np
from PIL import Image


class Square:

    def __init__(self, x_axis, y_axis, side, color):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.side = side
        self.color = color

    def draw(self, canvas):
        self.canvas = canvas
        pass


class Rectangle:

    def __init__(self, x_axis, y_axis, width, height, color):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        self.canvas = canvas
        pass

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, imagepath):
        self.imagepath = imagepath
        pass
