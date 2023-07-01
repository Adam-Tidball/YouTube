import turtle

# Define the data for the bar graph
data = [50, 80, 120, 200, 100]  # Sample data values

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Bar Graph")
screen.bgcolor("black")

# Set up the turtles
bar_width = 40      # Width of each bar
bar_spacing = 20    # Spacing between bars
bar_color = "blue"  # Color of the bars

# Calculate the total width required for the bar graph
graph_width = (bar_width + bar_spacing) * len(data) - bar_spacing

# # Position the turtles at the starting point
x_start = -graph_width / 2    # Starting x-coordinate adjusted for the graph width
y_start = -150                # Starting y-coordinate

# Create and position the turtles
turtles = []
for i in range(len(data)):
    x = x_start + (bar_width + bar_spacing) * i
    y = y_start

    # Create a turtle for each bar
    bar_turtle = turtle.Turtle()
    bar_turtle.shape("square")
    bar_turtle.color(bar_color)
    bar_turtle.penup()
    bar_turtle.goto(x, y)
    bar_turtle.shapesize(stretch_wid=data[i] / 20, stretch_len=1)
    bar_turtle.stamp()

    turtles.append(bar_turtle)

# Close the turtle graphics window
turtle.done()
