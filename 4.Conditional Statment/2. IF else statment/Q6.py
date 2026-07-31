# Write a Python program to:
# Take a number from the user
# If the number is divisible by 2 and 3, print:
# Divisible by 2 and 3
# Otherwise, print:
# Not Divisible by 2 and 3
# Example
# Input:
# 12
# Output:
# Divisible by 2 and 3
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print("Divisible by 2 and 3")
else:
    print("Not Divisible by 2 and 3")