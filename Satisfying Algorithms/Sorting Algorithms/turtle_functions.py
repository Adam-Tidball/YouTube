import turtle

def create_turtles(screen, data):
    # Get the screen size
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    # Calculate the top right coordinates
    right_x = screen_width/2
    top_y = screen_height/2

    # Set up the turtles
    bar_spacing = 40    # Spacing between bars

    # Position the turtles at the starting point
    x_start = -right_x + bar_spacing    # Starting x-coordinate adjusted for the graph width
    y_start = -150 
    turtles = []
    for i in range(len(data)):
        x = x_start + (bar_spacing) * i
        y = y_start + data[i]/2

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

def change_shape_colors(turtles, colors):
    for i, turtle_obj in enumerate(turtles):
        color = colors[i % len(colors)]
        turtle_obj.color(color)

def swap_positions(turtles, index1, index2):
    if len(turtles) >= 2:
        temp_pos = turtles[index1].pos()
        turtles[index1].clear()
        turtles[index1].setpos(turtles[index2].pos())
        turtles[index2].setpos(temp_pos)

def make_screen():
    screen = turtle.Screen()
    screen.title("Switching Shape Positions")
    screen.bgcolor("black")
    return screen

 
def close_screen():
    turtle.done()
