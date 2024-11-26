sum = 0  # Initialize the sum to 0
print("Enter the value of n: ")  # Prompt user to enter how many numbers they want to add
n = int(input())  # Input the number of values
print("Enter " + str(n) + " numbers: ")  # Prompt user to enter the numbers

# Loop to input 'n' numbers and add them to the sum
for i in range(n):
    num = int(input())  # Take each number as input
    sum = sum + num  # Add the number to the sum

# Output the total sum
print("Sum of " + str(n) + " numbers = " + str(sum))
