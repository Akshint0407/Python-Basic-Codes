# Getting input values from the user
m = float(input("Enter a number for the angle (in radians): "))  # You can input angle in radians
operation = input("Enter the operation to run (sin/cos): ").lower()  # The user can input 'sin' or 'cos'

# Importing the necessary functions from the math module
from math import sin, cos, radians

# If the user inputs "sin", calculate sine of the angle
if operation == "sin":
    print("The sine of", m, "is:", sin(m))  # Using sin() function from math module

# If the user inputs "cos", calculate cosine of the angle
elif operation == "cos":
    print("The cosine of", m, "is:", cos(m))  # Using cos() function from math module

# If the input operation is not recognized
else:
    print("Invalid operation! Please enter 'sin' or 'cos'.")
