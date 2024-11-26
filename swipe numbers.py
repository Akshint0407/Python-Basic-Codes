# Input two values
num1 = int(input("Enter the 1st value:"))
num2 = int(input("Enter the 2nd value:"))

# Swapping the values using a temporary variable
temp = num1  # Store the value of num1 in temp
num1 = num2  # Assign the value of num2 to num1
num2 = temp  # Assign the value of temp (original num1) to num2

# Print the swapped values
print("Swapped values are:", num1, num2)
