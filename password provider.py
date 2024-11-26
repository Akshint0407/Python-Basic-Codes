import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}[]()*;/,$%^&@"

all = lower + upper + numbers + symbols  # Combine all characters
length = 19  # Length of the password
password = "".join(random.sample(all, length))  # Randomly select characters to form the password

print(password)
