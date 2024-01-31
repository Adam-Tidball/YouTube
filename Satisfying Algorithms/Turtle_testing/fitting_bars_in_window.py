import turtle

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
bar_width = 5  
bar_spacing = 50 
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



# Close the turtle graphics window
turtle.done()


print("DONE")