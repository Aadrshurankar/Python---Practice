# Write a Python program to:

# Take two numbers from user
# Print:
# "First is greater" if first number > second
# "Second is greater" if second > first
# "Both are equal" if both are same
# Example

# Input:

# 10
# 20

# Output:

# Second is greater
# 👉 Write your code 👨‍💻

# Take two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First is greater")
elif num2 > num1:
    print("Second is greater")
else:
    print("Both are equal")