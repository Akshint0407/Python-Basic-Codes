# List of numbers from 1 to 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the initial list
print("The list is \n", A)

# Output using for loop
print("The output for for loop is \n")
for i in A:
    print(i, "\t")  # Printing each element of the list with a tab space

# Output using while loop
print("Output for while loop \n")
i = 0
while(i < len(A)):  # Use len(A) to make the loop more flexible
    print(i, i, A[i], "\t")  # Printing index, index value, and element at A[i]
    i = i + 1

# Message indicating the end of the loops
print("Outside the loops \n")
