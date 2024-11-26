# Program to verify the algebraic expansion: (a + b)^2 = a^2 + 2ab + b^2

# Input: Taking two integers 'a' and 'b' from the user
a = int(input("Enter value of a: "))  # Asking the user to input the first number
b = int(input("Enter value of b: "))  # Asking the user to input the second number

# Step 1: Calculating the left-hand side of the equation (a + b)^2
lhs = (a + b) ** 2

# Step 2: Calculating the right-hand side of the equation a^2 + 2ab + b^2
rhs = a**2 + 2 * (a * b) + b**2

# Step 3: Checking if the two sides are equal
is_equal = lhs == rhs  # This will be True if both sides are equal, otherwise False

# Step 4: Printing the results
print(f"The value of (a + b)^2 is: {lhs}")
print(f"The value of a^2 + 2ab + b^2 is: {rhs}")
print(f"Are both sides equal? {is_equal}")  # Will display True if the equation holds
