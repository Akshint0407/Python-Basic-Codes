# Calculator Program with various functionalities

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def sub(x, y):
    return x - y

# Function to multiply two numbers
def multi(x, y):
    return x * y

# Function to divide two numbers
def div(x, y):
    if y == 0:  # Prevent division by zero
        return "Division by zero is not allowed"
    return x / y

# Function to calculate power (x^y)
def power(x, y):
    return x ** y

# Function to calculate factorial
def factorial(x):
    factorial = 1
    if x < 0:  # Factorial is not defined for negative numbers
        return "Factorial not defined for negative numbers"
    elif x == 0:  # Factorial of 0 is 1
        return 1
    else:
        for i in range(1, x + 1):
            factorial *= i  # Multiply each number from 1 to x
    return factorial

# Main program loop
while True:
    # Display menu options
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Factorial")
    print("7. Exit")

    # User input for choice
    choice = int(input("Enter your choice (1-7): "))

    # Perform the selected operation
    if choice == 1:
        n1 = int(input("Enter first number (n1): "))
        n2 = int(input("Enter second number (n2): "))
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == 2:
        n1 = int(input("Enter first number (n1): "))
        n2 = int(input("Enter second number (n2): "))
        print(f"{n1} - {n2} = {sub(n1, n2)}")
    elif choice == 3:
        n1 = int(input("Enter first number (n1): "))
        n2 = int(input("Enter second number (n2): "))
        print(f"{n1} * {n2} = {multi(n1, n2)}")
    elif choice == 4:
        n1 = int(input("Enter first number (n1): "))
        n2 = int(input("Enter second number (n2): "))
        print(f"{n1} / {n2} = {div(n1, n2)}")
    elif choice == 5:
        n1 = int(input("Enter base number (n1): "))
        n2 = int(input("Enter power (n2): "))
        print(f"{n1} ^ {n2} = {power(n1, n2)}")
    elif choice == 6:
        n1 = int(input("Enter a number (n1): "))
        print(f"{n1}! = {factorial(n1)}")
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
