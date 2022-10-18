import math, random

# TRYIT: Write a print statement that displays both the type and value of Pi
print("pi is a " + str(type(math.pi)) + " with a value of " + str(float(math.pi)))
# TRYIT: Write a conditional to print out if `i` is less than or greater than 50
def relationTo50(i):
    if int(i) > 50:
        print("i is greater than 50")
    elif int(i) < 50:
        print("i is less than 50")
    elif int(i) == 50:
        print("i is equal to 50")

# TRYIT: Write a conditional that prints the color of the picked fruit
def colorOfFruit(fruit):
    if fruit == 'orange':
        print("the fruit is orange")
    elif str(fruit) == "apple":
        print("the fruit is red")
    elif str(fruit) == "banana":
        print("the fruit is yellow")
    else: 
        print("the fruit isn't in our database")

# TRYIT: Write a function that multiplies two numbers and returns the result
def multiply(num1,num2):
    answer = int(num1) * int(num2)
    print(str(num1) + " x " + str(num2) + " = " + str(answer))
    return answer

# TRYIT: Write a function that multiplies two numbers and returns the result


# TRYIT: Now call the function a few times to calculate the following answers
i = input("Please input the value of i: ")
relationTo50(i)
fruit = input("Please input fruit name: ")
colorOfFruit(fruit)
multiply(12,96)
multiply(48,17)
multiply(196523,87323)


