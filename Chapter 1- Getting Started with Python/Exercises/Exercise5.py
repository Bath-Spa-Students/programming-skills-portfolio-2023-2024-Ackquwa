# Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

# Defining a function to compute for the area of the circle when given radius.
def compute(radius):
    
    # Formula for are of a circle
    return math.pi * radius * radius * 2
         # pi value

def main():
    # Here is where it takes a user unput as a "float" function.
    radius = float(input("Enter the Radius of the circle: "))
    
    # Call the compute_circle_area function with the entered radius.
    area = compute (radius)
    
    # Print the already computed area of the circle.
    print("The area of the circle with radius", radius, "is:", area)

if __name__ == "__main__":
    main()