import turtle
import sys
import os

# Get the absolute path of the parent directory (main_folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Access visualization & sound functions 
import sorting_sounds

# Global Variables
base_color = "Blue"
highlight_color = "Green"

def make_screen():
    screen = turtle.Screen()
    screen.title("Switching Shape Positions")
    screen.bgcolor("Black")
    return screen
 
def close_screen():
    turtle.done()

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
    x_start = -right_x + bar_spacing    # Starting x-coordinate far left
    y_start = -150 
    turtles = []
    for i in range(len(data)):
        x = x_start + (bar_spacing) * i
        y = y_start + data[i]/2

        # Create a turtle for each bar
        bar_turtle = turtle.Turtle()
        bar_turtle.speed(0)
        bar_turtle.shape("square")
        bar_turtle.color(base_color)
        bar_turtle.penup()
        bar_turtle.goto(x, y)

        # Stamp the rectangle shape
        bar_turtle.shapesize(stretch_wid=data[i] / 20, stretch_len=1)
        bar_turtle.stamp()

        # Make a noise after each stamp
        sorting_sounds.play_NotificationOne()

        # Add turtle to list
        turtles.append(bar_turtle)

    #return created turtle list
    return turtles

def swap_positions(turtles, index1, index2):
    if len(turtles) >= 2:
        # Set swap speed
        turtles[index1].speed(0)
        turtles[index2].speed(0)

        # Swap turtle positions
        temp_xpos = turtles[index1].xcor()
        turtles[index1].clear()
        turtles[index1].setx(turtles[index2].xcor())
        turtles[index2].clear()
        turtles[index2].setx(temp_xpos)

        # Swap turtle objects 
        turtles[index1], turtles[index2] = turtles[index2], turtles[index1]


def drop_all(screen, turtles):
    screen_height = screen.window_height()
    for turtle in turtles:
        turtle.speed(9)
        turtle.penup()
        turtle.sety(-screen_height)  # Set y-coordinate off the screen



def highlight_current(turtles, index):
    arr_size = len(turtles)
    if index is 0:
        turtles[index].color(highlight_color)
    elif 0 < index < arr_size:
        turtles[index - 1].color(base_color)
        turtles[index].color(highlight_color)
    elif index is arr_size:
        turtles[index - 1].color(base_color)
    else:
        pass




def change_shape_colors(turtles, colors):
    for i, turtle_obj in enumerate(turtles):
        color = colors[i % len(colors)]
        turtle_obj.color(color)
