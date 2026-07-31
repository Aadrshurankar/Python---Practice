# Write a Python program to:
# Take a number from the user
# If the number is a multiple of 10, print:
# Multiple of 10
# Otherwise, print:
# Not a Multiple of 10
# Example
# Input:
# 25
# Output:
# Not a Multiple of 10
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")