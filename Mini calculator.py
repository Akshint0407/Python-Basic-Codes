# Taking input for two numbers (a and b) and the operation choice (n)
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
n = int(input("Choose your operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

# Checking the operation chosen by the user
if (n == 1):
    # If the user chose 1, perform addition
    print(a + b)
elif (n == 2):
    # If the user chose 2, perform subtraction
    print(a - b)
elif (n == 3):
    # If the user chose 3, perform multiplication
    print(a * b)
elif (n == 4):
    # If the user chose 4, perform division
    # (Ensure that division by zero is handled in real applications)
    print(a / b)
else:
    # If the user enters an invalid operation choice
    print("Invalid choice! Please choose a valid operation.")
