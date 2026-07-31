# Write a Python program to:
# Take a number from the user
# If the number is divisible by 2, print:
# Divisible by 2
# Else if the number is divisible by 3, print:
# Divisible by 3
# Otherwise, print:
# Not Divisible by 2 or 3
# Example
# Input:
# 9
# Output:
# Divisible by 3
# Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Divisible by 2")
elif number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 2 or 3")