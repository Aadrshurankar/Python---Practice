# Write a Python program to:
# Find the factorial of a number
# Take input from the user
# Use a for loop
# Example
# Input:
# 5
# Output:
# 120
# Because:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 👉 Write your code 👨‍💻


# Take input from the user
number = int(input("Enter a number: "))
fact = 1
for i in range(1, number + 1):
    fact *= i
print(fact)