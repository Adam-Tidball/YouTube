import turtle
import time

# Define the data for the bar graph
data = [50, 80, 120, 200, 100]  # Sample data values

# Set up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Set the drawing speed (0 is the fastest)
bar_width = 40      # Width of each bar
bar_spacing = 20    # Spacing between bars

# Calculate the total width required for the bar graph
graph_width = (bar_width + bar_spacing) * len(data) - bar_spacing

# Position the turtle at the starting point
x_start = -graph_width / 2    # Starting x-coordinate adjusted for the graph width
y_start = -150                # Starting y-coordinate
my_turtle.penup()
my_turtle.goto(x_start, y_start)
my_turtle.pendown()

# Draw the bars
my_turtle.penup()
for i in range(len(data)):
    value = data[i]

    my_turtle.pendown()
    my_turtle.begin_fill()          # Begin filling the bar
    my_turtle.left(90)              # Turn left to draw the bar upwards
    my_turtle.forward(value)        # Draw the bar
    my_turtle.right(90)             # Turn right to prepare for the next bar
    my_turtle.forward(bar_width)    # Move to the next bar's position
    my_turtle.right(90)             # Turn right to face downward
    my_turtle.forward(value)        # Draw the bottom part of the bar
    my_turtle.left(90)              # Turn left to prepare for the next bar
    my_turtle.end_fill()            # End filling the bar
    my_turtle.penup()
    my_turtle.forward(bar_spacing)  # Move to the next bar's starting position


#Draw over the set up bars
my_turtle.goto(x_start, y_start)
time.sleep(3)
my_turtle.fillcolor("blue")

for i in range(len(data)):
    value = data[i]

    # Swap the positions of the first and last rectangles
    if i == 0:
        value = data[-1]
    elif i == len(data) - 1:
        value = data[0]

    my_turtle.pendown()
    my_turtle.begin_fill()          # Begin filling the bar
    my_turtle.left(90)              # Turn left to draw the bar upwards
    my_turtle.forward(value)        # Draw the bar
    my_turtle.right(90)             # Turn right to prepare for the next bar
    my_turtle.forward(bar_width)    # Move to the next bar's position
    my_turtle.right(90)             # Turn right to face downward
    my_turtle.forward(value)        # Draw the bottom part of the bar
    my_turtle.left(90)              # Turn left to prepare for the next bar
    my_turtle.end_fill()            # End filling the bar
    my_turtle.penup()
    my_turtle.forward(bar_spacing)  # Move to the next bar's starting position


# Close the turtle graphics window
turtle.done()
