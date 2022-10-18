## TRYIT: Import the required math functions
from math import degrees, sqrt, atan

# TRYIT: Create variables to store the triangle sides input by the user
slideHeight = input("Enter the rise of the slide's ladder: ")
slideWidth = input("Enter the run of the base of the slide: ")
#slideLength = input("")
#slideSlope = input("")

# TRYIT: Use the int() function to convert the input string values to integers
slideHeight = int(slideHeight)
slideWidth = int(slideWidth)

# TRYIT: Calculate the values
slideLength = sqrt((slideHeight ** 2) + (slideWidth ** 2))
slideAngle = degrees(atan(slideHeight/slideWidth))

# TRYIT: Create a Boolean variable to store true or false if the slide length meets safety standards
safeSlide = False

# TRYIT: Create an if...elif...else statement to test the measurements of the slide
if slideAngle < 40 and slideHeight <= 6:
    safeSlide = True
else:
    safeSlide = False

# TRYIT Use an if...else statement to test whether the Boolean variable is True or False, and print the results
if safeSlide:
    print("Safe! The angle is: " + str(int(slideAngle)) + " and your slide length is: " + str(int(slideLength)))
else:
    print("Unsafe! The angle is: " + str(int(slideAngle)) + " and your slide length is: " + str(int(slideLength)))

