import turtle
import time

##############################################################
# Note -> The start of this code is fitting_bars_in_window.py

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1282, height=720, startx=None, starty=None)
screen.title("Bar Graph")
screen.bgcolor("#212121")

# Get the screen size
screen_width = screen.window_width()
screen_height = screen.window_height()

# Calculate the top right coordinates
right_x = screen_width/2
left_x = -right_x
top_y = screen_height/2
bottom_y = - top_y

# Set up the turtles
bar_width = 15  
bar_spacing = 100 
bar_color = "blue" 
turtle.mode("logo") 

# Find the number of bars to put on the screen
sect_size = bar_width + bar_spacing
num_sect = int((screen_width - bar_spacing) / sect_size)
print("number of sections: ", num_sect)

# Adjust inital spacing
remainder = (screen_width - bar_spacing) % sect_size 
first_space = bar_spacing + remainder/2
start_x = left_x + first_space
start_y = 0


# # Create and position the turtles
# bar_turtle = turtle.Turtle()
# bar_turtle.speed(1)
# bar_turtle.shape("square")
# bar_turtle.color("blue")
# bar_turtle.goto(start_x, 0)

# Create and position the turtles
turtles = []
for i in list(range(0, num_sect)):
    x = start_x + sect_size * i
    y = 0 # Need to change to make bottoms even 

    # Create a turtle for each bar
    bar_turtle = turtle.Turtle()
    bar_turtle.speed(0)
    bar_turtle.shape("square")
    bar_turtle.color("blue")
    bar_turtle.penup()
    bar_turtle.goto(x, y)

    # Stamp the rectangle shape
    bar_turtle.resizemode("user")
    bar_turtle.shapesize(stretch_wid= bar_width/10, stretch_len= 10) # place holder len
    bar_turtle.stamp()

    turtles.append(bar_turtle)


################################################
# This is the start of Testing droping the bars 

#-----------------#
# This section causes all of the turtles to instant jump 
# using the screen tracer() function 
       
time.sleep(1)
print("Time to drop!")

screen.tracer(False)  # disable updating view on screen

for turt in turtles:
    turt.clear()
    turt.speed(9)
    turt.penup()
    turt.sety(-250)  # Set y-coordinate off the screen

# when you are ready to see the whole screen update
screen.update()
screen.tracer(True)  # enable updating view on screen 

#------------------#
# This section causes the turtles to move
# more continuously 

time.sleep(1)
print("Time to rise!")

screen.tracer(False)  # disable updating view on screen

x = -250
while x < 50:
    for turt in turtles:
        turt.clear()
        turt.speed(9)
        turt.penup()
        turt.sety(x)  # Set y-coordinate off the screen
    screen.update()
    # time.sleep(0.01)  # control speed
    x = x + 1

######### def drop_all_together(screen, turtles):

screen.tracer(False)  # disable updating view on screen

screen_height = screen.window_height()
ypos = turtles[0].ycor() # set to fisrt turles y corrdinate
drop_by = 1 # control drop amount
while ypos > -screen_height:
    for turt in turtles:
        turt.speed(9)
        turt.penup()
        turt.sety(ypos)  # Set y-coordinate off the screen
    screen.update()
    ypos = ypos - drop_by



# Close the turtle graphics window
turtle.done()


print("DONE")