# Write a Python program to:
# Take a number from the user
# If the number is divisible by 5, print:
# Divisible by 5
# Otherwise, print:
# Not Divisible by 5
# Example
# Input:
# 12
# Output:
# Not Divisible by 5
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")