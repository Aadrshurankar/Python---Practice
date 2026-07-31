# Write a Python program to:
# Take a number from the user
# If the number is divisible by 2, print:
# Even Number
# Otherwise, print:
# Odd Number
# Example
# Input:
# 7
# Output:
# Odd Number
# 👉 Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")