# Program to demonstrate string formatting in Python using the '%' operator

# Step 1: Assigning values to variables
name = 'Parth'               # The name of the student
course = 'Chemical Engg'     # The course the student is enrolled in
age = 19                     # The age of the student

# Step 2: Using string formatting to display the values
# The '%s' is used as a placeholder for strings, and '%d' is for integers.
print("name = %s and course = %s and age = %d" % (name, course, age))

# Step 3: Directly formatting values in the string without using variables
# Here, 'Anand', 'Mechanical Engg', and 20 are passed directly into the format placeholders.
print("name = %s and course = %s and age = %d" % ('Anand', 'Mechanical Engg', 20))
