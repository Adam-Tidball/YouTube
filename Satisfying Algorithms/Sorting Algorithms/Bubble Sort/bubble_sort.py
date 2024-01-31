# Code based on the following: https://www.geeksforgeeks.org/bubble-sort/

import sys
import os
import time

# Get the absolute path of the parent directory (main_folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Access visualization & sound functions 
import turtle_functions
import sorting_sounds

# Global variables & data definition 
my_screen = turtle_functions.make_screen()

my_turtles, arr = turtle_functions.create_random_turtles(my_screen)
time.sleep(0.5)

# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):

    n = len(arr)
    print(n)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            my_turtles[j].color("Dark Red")
            # sorting_sounds.play_NotificationFour()
            time.sleep(0.1)         # this wait it partly for the bar to turn red

            my_turtles[j].color("Blue")
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                turtle_functions.swap_positions(my_turtles,j,j+1)
                my_turtles[j].color("Blue")

    
        my_turtles[n-i-1].color("Green")
        # sorting_sounds.play_NotificationThree()
        # time.sleep(0.5)


# Driver code to test above
def main():

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        
# After main start closing sequence on sorted array
if __name__ == "__main__":

    main()

    #insert final sorted array effects
    #turtle_functions.drop_all_one_by_one(my_screen, my_turtles)
    
    turtle_functions.drop_all_together_to_even(my_screen, my_turtles)
    turtle_functions.drop_all_together_off_screen(my_screen, my_turtles)
    
    turtle_functions.close_screen()

    
  