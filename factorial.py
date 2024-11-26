# Program to calculate the factorial of a number.

# Step 1: Take input from the user for the number
num = int(input("Enter the value: "))

# Step 2: Initialize the factorial variable to 1
factorial = 1

# Step 3: Check if the number is negative (factorial is not valid for negative numbers)
if (num < 0):
    print("Not Valid")  # Factorial is not defined for negative numbers

# Step 4: If the number is 0 or 1, return factorial as 1
elif (num == 0 or num == 1):
    print("Factorial of", num, "is 1")  # The factorial of 0 and 1 is always 1

# Step 5: For numbers greater than 1, calculate the factorial using a loop
else:
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        factorial = factorial * i  # Multiply the current value of factorial by the current number in the loop
    print("Factorial of", num, "is", factorial)  # Output the calculated factorial
