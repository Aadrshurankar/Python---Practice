# Write a Python program to:
# Take a number from the user
# If the number is greater than 0, print:
# Positive
# Else if the number is equal to 0, print:
# Zero
# Otherwise, print:
# Negative
# Example
# Input:
# -10
# Output:
# Negative
# Write your code 👨‍💻

number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")