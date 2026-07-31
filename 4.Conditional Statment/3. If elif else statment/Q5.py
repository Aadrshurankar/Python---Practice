# Write a Python program to:
# Take a number from the user
# If the number is less than 10, print:
# Small Number
# Else if the number is less than 100, print:
# Medium Number
# Otherwise, print:
# Large Number
# Example
# Input:
# 50
# Output:
# Medium Number
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number < 10:
    print("Small Number")
elif number < 100:
    print("Medium Number")
else:
    print("Large Number")