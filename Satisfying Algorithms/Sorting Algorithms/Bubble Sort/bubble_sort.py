# Code based on the following: https://www.geeksforgeeks.org/bubble-sort/

import sys
import os
import time

# Get the absolute path of the parent directory (main_folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Access visualization functions
import turtle_functions

# Global variables & data definition 
my_screen = turtle_functions.make_screen()
#arr = [600, 300 , 100, 500]
arr = [50, 80, 120, 200, 100,
        40, 20, 230, 160, 140,
        190, 50, 220, 70, 90]
my_turtles = turtle_functions.create_turtles(my_screen, arr)
time.sleep(2)

# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):

    n = len(arr)
    print(n)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            my_turtles[j].color("Green")
            time.sleep(0.5)
            my_turtles[j].color("Blue")
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                turtle_functions.swap_positions(my_turtles,j,j+1)
                my_turtles[j].color("Blue")


        my_turtles[n-i-1].color("Purple")


# Driver code to test above
def main():

    bubbleSort(arr)
  
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        
# After main start closing sequence on sorted array
if __name__ == "__main__":
    main()
    #### insert final sorted array effect
    turtle_functions.close_screen()

    
  