# Write a Python program to:
# Take a number from the user
# If the number is greater than 0, print:
# Positive
# Else if the number is less than 0, print:
# Negative
# Otherwise print:
# Zero
# Example
# Input:
# -5
# Output:
# Negative
# 👉 Write your code 👨‍💻

number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")