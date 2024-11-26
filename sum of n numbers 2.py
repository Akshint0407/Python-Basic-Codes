# Ask the user for the number of values they want to sum
n = int(input("Enter the number of values:"))

# Initialize the sum to 0
sum_no = 0

# Loop to input 'n' numbers and calculate their sum
for i in range(n):
    no = int(input(f"Enter number {i + 1}: "))  # Prompt user with the number position
    sum_no += no  # Add the number to sum_no

# Print the total sum
print("Sum of all numbers is:", sum_no)
