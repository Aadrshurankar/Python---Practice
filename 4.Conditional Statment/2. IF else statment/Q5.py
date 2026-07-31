# Write a Python program to:
# Take two numbers from the user
# If the first number is greater than the second number, print:
# First Number is Greater
# Otherwise, print:
# Second Number is Greater or Equal
# Example
# Input:
# 20
# 15
# Output:
# First Number is Greater
# Write your code 👨‍💻

# Taking two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Comparing the numbers
if num1 > num2:
    print("First Number is Greater")
else:
    print("Second Number is Greater or Equal")