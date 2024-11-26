# Program to print a message while 'count' satisfies the condition

# Step 1: Take user input for the starting value of count
count = int(input("Enter the starting value of count: "))

# Step 2: Loop to print a message 10 times if count is greater than 10
# The loop runs while count is greater than 10
while count > 10:
    print("Maths subject")
    count = count - 1  # Decrement count to eventually exit the loop

# Step 3: When the loop condition is no longer true, the else block executes
else:
    print("Message printed until count dropped below or equal to 10!")
