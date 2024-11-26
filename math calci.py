# Importing the math module to use math.pow for exponentiation
import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def sub(x, y):
    return x - y

# Function to multiply two numbers
def mult(x, y):
    return x * y

# Function to divide two numbers
def div(x, y):
    return x / y

# Function to calculate x raised to the power of y
def x_power(x, y):
    return math.pow(x, y)  # Using math.pow to calculate x^y

# Function to calculate the factorial of a number
def x_factorial(x):
    factorial = 1
    if x == 0:  # Factorial of 0 is 1
        return factorial
    else:
        for i in range(1, x + 1):
            factorial = factorial * i  # Multiply the result by each number from 1 to x
    return factorial

# Main program loop
while True:
    # Displaying the main menu
    print("Main Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. x^y")
    print("6. x!")
    print("7. Exit")
    
    # Taking user input for the choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # If the choice is 1, perform addition
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        print(n1, "+", n2, "=", add(n1, n2))
        
    elif choice == 2:
        # If the choice is 2, perform subtraction
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        print(n1, "-", n2, "=", sub(n1, n2))
        
    elif choice == 3:
        # If the choice is 3, perform multiplication
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        print(n1, "*", n2, "=", mult(n1, n2))
        
    elif choice == 4:
        # If the choice is 4, perform division
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        print(n1, "/", n2, "=", div(n1, n2))
        
    elif choice == 5:
        # If the choice is 5, perform exponentiation (x^y)
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        print(n1, "^", n2, "=", x_power(n1, n2))
        
    elif choice == 6:
        # If the choice is 6, calculate factorial of n1
        n1 = int(input("n1 = "))
        print(n1, "!", "=", x_factorial(n1))
        
    elif choice == 7:
        # If the choice is 7, exit the program
        print("Exiting!")
        break  # Breaks the loop and ends the program
