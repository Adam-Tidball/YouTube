import turtle
import random
import time
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
    screen.setup(width=1282, height=720, startx=None, starty=None)
    screen.title("Dark Grey Screen")
    screen.bgcolor("#212121")
    return screen
 
def close_screen():
    turtle.done()

def get_rand_length():
    return random.randint(1, 30)

def create_random_turtles(screen):
    # Get the screen size
    screen_width = screen.window_width()
    screen_height = screen.window_height()

    # Calculate the screen coordinates
    right_x = screen_width/2
    left_x = -right_x
    top_y = screen_height/2
    bottom_y = - top_y

    # Set up the turtles
    bar_width = 2  
    bar_spacing = 10 
    turtle.mode("logo") # Starting orientation North 

    # Find the number of bars to put on the screen
    sect_size = bar_width + bar_spacing
    num_sect = int((screen_width - bar_spacing) / sect_size)

    # Adjust inital spacing
    remainder = (screen_width - bar_spacing) % sect_size 
    first_space = bar_spacing + remainder/2
    x_start = left_x + first_space
    y_start = 0

    # Position the turtles at the starting point
    turtles = []
    arr = []
    for i in list(range(0, num_sect)):

        # Generate number to sort   
        ran_len = get_rand_length()

        x = x_start + sect_size * i
        #y = -300 + (ran_len*10) # to make bottoms even 
        y = 0

        # Create a turtle for each bar
        bar_turtle = turtle.Turtle()
        bar_turtle.speed(0)
        bar_turtle.shape("square")
        bar_turtle.color(base_color)
        bar_turtle.penup()
        bar_turtle.goto(x, y)

        # Stamp the rectangle shape
        bar_turtle.shapesize(stretch_wid= bar_width/10, stretch_len= ran_len)
        bar_turtle.stamp()

        # Make a noise after each stamp
        sorting_sounds.play_NotificationOne()

        # Add turtle to list
        turtles.append(bar_turtle)

        # Remove any turtle drawings
        bar_turtle.clear()

        # Add random length to list
        arr.append(ran_len)

    #return created turtle list
    return turtles, arr

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

        # Make a noise after each swap
        sorting_sounds.play_NotificationFour()

        # Swap turtle objects 
        turtles[index1], turtles[index2] = turtles[index2], turtles[index1]


def drop_all_one_by_one(screen, turtles):
    sorting_sounds.play_SwoopOne()

    screen_height = screen.window_height()
    for turt in turtles:
        turt.speed(9)
        turt.penup()
        turt.sety(-screen_height)  # Set y-coordinate off the screen

def drop_all_together_off_screen(screen, turtles):
    sorting_sounds.play_SwoopOne()

    screen.tracer(False)  # disable updating view on screen

    screen_height = screen.window_height()
    ypos = turtles[0].ycor() # set to fisrt turles y corrdinate
    drop_by = 1 # control drop amount
    while ypos > -screen_height:
        for turt in turtles:
            ypos = turt.ycor()
            ypos = ypos - drop_by
            turt.speed(9)
            turt.penup()
            turt.sety(ypos)  # Set y-coordinate off the screen
        screen.update()
        # ypos = ypos - drop_by

def drop_all_together_to_even(screen, turtles):
    sorting_sounds.play_SwoopOne()

    screen.tracer(False)  # disable updating view on screen

    screen_height = screen.window_height()
    ypos = turtles[0].ycor() # set to fisrt turles y corrdinate
    drop_by = 1 # control drop amount
    while ypos > -screen_height:
        for turt in turtles:
            turt.speed(9)
            turt.penup()

            turt_size = turt.shapesize()
            y = -300 + (turt_size[1]*10) #Takes the x size of the turt
            if ypos >= y:
                turt.sety(ypos)  # Set y-coordinate 

        screen.update()
        ypos = ypos - drop_by


def highlight_current(turtles, index):
    arr_size = len(turtles)
    if index == 0:
        turtles[index].color(highlight_color)
    elif 0 < index < arr_size:
        turtles[index - 1].color(base_color)
        turtles[index].color(highlight_color)
    elif index == arr_size:
        turtles[index - 1].color(base_color)
    else:
        pass




def change_shape_colors(turtles, colors):
    for i, turtle_obj in enumerate(turtles):
        color = colors[i % len(colors)]
        turtle_obj.color(color)
