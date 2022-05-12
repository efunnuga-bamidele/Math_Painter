from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
canvas_color = (input("Enter canvas color (white || black || red || green || blue )")).lower()

canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw (rectangle or square)? Enter 'quit' to exit application. ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x_axis of the rectangle: "))
        rec_y = int(input("Enter y_axis of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        rectangle = Rectangle(x_axis=rec_x, y_axis=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        rectangle.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == 'square':
        squ_x = int(input("Enter x_axis of the square: "))
        squ_y = int(input("Enter y_axis of the square: "))
        squ_side = int(input("Enter size of the sides: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        square = Square(x_axis=squ_x, y_axis=squ_y, side=squ_side, color=(red, green, blue))
        square.draw(canvas)
    if shape_type.lower() == "quit":
        break
canvas.make("canvas.png")

