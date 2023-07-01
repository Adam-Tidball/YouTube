#testing shapes with turtle

from turtle import *

# color('red','yellow')
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# Turtle.shape("triangle")
# screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))


# Create a turtle object
my_turtle = Turtle()

# Set the turtle speed (optional)
my_turtle.speed(10)

# Draw the rectangle
for _ in range(4):
    my_turtle.forward(100)   # Move forward by 100 units
    my_turtle.right(90)      # Turn right by 90 degrees

# Close the turtle graphics window
done()