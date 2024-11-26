# Program to check whether a number is even or odd.

# Step 1: Take input from the user for the number
n = int(input("Enter the number: "))

# Step 2: Check if the number is divisible by 2 (even) or not (odd)
if (n % 2 == 0):  # If the remainder when divided by 2 is 0, it's even
    print("Even")  # Output: 'Even' if the condition is true
else:
    print("Odd")  # Output: 'Odd' if the condition is false
