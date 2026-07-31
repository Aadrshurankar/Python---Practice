# Write a Python program to:
# Take a number n from the user
# Find the factorial of a number using while loop
# If the number is negative, print:
# Factorial not possible
# Example 1
# Input:
# 5
# Output:
# 120
# Example 2
# Input:
# -3
# Output:
# Factorial not possible
# 👉 Write your code


n = int(input("Enter a number: "))
if n < 0:
    print("Factorial not possible")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(factorial)