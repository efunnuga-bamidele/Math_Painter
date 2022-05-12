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