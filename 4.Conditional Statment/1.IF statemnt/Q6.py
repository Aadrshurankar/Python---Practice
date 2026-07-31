# Write a Python program to:
# Take a number from the user
# If the number is divisible by both 3 and 5, print:
# Divisible by 3 and 5
# Example
# Input:
# 15
# Output:
# Divisible by 3 and 5
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by 3 and 5")