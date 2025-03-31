# Program to find the greatest of three numbers.

# Step 1: Take input for the three numbers
n1 = int(input("Enter the 1st value: "))
n2 = int(input("Enter the 2nd value: "))
n3 = int(input("Enter the 3rd value: "))

# Step 2: Compare the first number (n1) with the other two numbers
if (n1 > n2):  # Check if n1 is greater than n2
    if (n1 > n3):  # If n1 is also greater than n3, then n1 is the greatest
        print("n1 is greater!")
    else:  # If n1 is not greater than n3, then n3 is the greatest
        print("n3 is greater!")
elif (n2 > n3):  # If n1 is not greater than n2, compare n2 and n3
    print("n2 is greater!")  # If n2 is greater than n3, n2 is the greatest
else:  # If n2 is not greater than n3, then n3 is the greatest
    print("n3 is greater!")
