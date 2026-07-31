# Write a Python program to:
# Find the factorial of a number
# Take input from the user
# Use a while loop
# Example
# Input:
# 5
# Output:
# 120
# Because:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 👉 Write your code 👨‍💻

n = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("The factorial of", n, "is", factorial)