import turtle

# Define the data for the bar graph
data = [50, 80, 120, 200, 100,
        40, 20, 230, 160, 140,
        190, 50, 220, 70, 90]  # Sample data values

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Bar Graph")
screen.bgcolor("black")

# Set up the turtles
bar_spacing = 40    # Spacing between bars
bar_color = "blue"  # Color of the bars

# Get the screen size
screen_width = screen.window_width()
screen_height = screen.window_height()

# Calculate the top right coordinates
right_x = screen_width/2
top_y = screen_height/2

# The center coordinates
center_x = 0
center_y = 0

# Position the turtles at the starting point
x_start = -right_x + bar_spacing    # Starting x-coordinate adjusted for the graph width
y_start = -150               # Starting y-coordinate

# Create and position the turtles
turtles = []
for i in range(len(data)):
    x = x_start + (bar_spacing) * i
    y = y_start + (data[i]/2)

    # Create a turtle for each bar
    bar_turtle = turtle.Turtle()
    bar_turtle.speed(0)
    bar_turtle.shape("square")
    bar_turtle.color("blue")
    bar_turtle.penup()
    bar_turtle.goto(x, y)

    # Stamp the rectangle shape
    bar_turtle.shapesize(stretch_wid=data[i] / 20, stretch_len=1)
    bar_turtle.stamp()

    turtles.append(bar_turtle)

# Close the turtle graphics window
turtle.done()
