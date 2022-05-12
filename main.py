import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        # self.imagepath = imagepath
        self.img = Image.fromarray(self.data, 'RGB')
        self.img.save(imagepath)
        pass


class Square:

    def __init__(self, x_axis, y_axis, side, color):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.side = side
        self.color = color

    def draw(self, canvas):
        # self.canvas = canvas
        canvas.data[self.x_axis:self.x_axis + self.side, self.y_axis:self.y_axis + self.side] = self.color


class Rectangle:

    def __init__(self, x_axis, y_axis, width, height, color):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x_axis:self.x_axis + self.width, self.y_axis:self.y_axis + self.height] = self.color

canvas = Canvas(width=200, height=200, color=(255, 255, 255))

square = Square(x_axis=10, y_axis=50, side=50, color=(100, 200, 125))
square.draw(canvas)

rectangle = Rectangle(x_axis=30, y_axis=100, width=50, height=65, color=(255, 0, 0))
rectangle.draw(canvas)
canvas.make("canvas.png")
