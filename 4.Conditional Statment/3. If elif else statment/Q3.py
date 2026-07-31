# Write a Python program to:
# Take a number from the user
# If the number is divisible by 15, print:
# Divisible by 15
# Else if the number is divisible by 5, print:
# Divisible by 5
# Otherwise, print:
# Not Divisible by 5 or 15
# Example
# Input:
# 30
# Output:
# Divisible by 15
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 15 == 0:
    print("Divisible by 15")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5 or 15")