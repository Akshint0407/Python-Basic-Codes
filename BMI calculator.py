# Program to calculate BMI (Body Mass Index)

# Step 1: Input height in meters
# The user is prompted to enter their height as a decimal (e.g., 1.65 meters)
height = input("Enter your height in meters (e.g., 1.65): ")

# Step 2: Input weight in kilograms
# The user is prompted to enter their weight as an integer or decimal (e.g., 72 kg)
weight = input("Enter your weight in kilograms (e.g., 72): ")

# Step 3: Convert the inputs to floating-point numbers
new_height = float(height)  # Convert height from string to float
new_weight = float(weight)  # Convert weight from string to float

# Step 4: Calculate BMI using the formula: weight / (height^2)
# BMI is cast to an integer for a cleaner output
BMI = int(new_weight / (new_height * new_height))

# Step 5: Print the calculated BMI
print(f"Your BMI is: {BMI}")
