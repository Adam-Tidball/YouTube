import turtle
import time

# Register the rectangle shape
turtle.register_shape("rectangle", ((-50, -25), (-50, 25), (50, 25), (50, -25)))

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the turtle shape to the registered rectangle
my_turtle.shape("rectangle")

x = 50
y = 50

time.sleep(5)

# Create a turtle object
my_turtle2 = turtle.Turtle()

# Register the rectangle shape
turtle.register_shape("triangle", ((-50 + x, -25 + y), (0, 0), (50 + x, -25 + y)))

# Set the turtle shape to the registered rectangle
my_turtle2.shape("triangle")

# Close the turtle graphics window
turtle.done()
