# Code based on the following: https://www.geeksforgeeks.org/bubble-sort/

import sys
import os
import turtle

# Get the absolute path of the parent directory (main_folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Access visualization functions
import turtle_functions


# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
      
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

# Driver code to test above
def main():
    #define array to be sorted
    arr = [20, 40 , 30, 10]
    turtle_functions.create_turtles(my_screen, arr)

    bubbleSort(arr)
  
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        
  

if __name__ == "__main__":

    my_screen = turtle_functions.make_screen()
    main()
    turtle_functions.close_screen()

    
  