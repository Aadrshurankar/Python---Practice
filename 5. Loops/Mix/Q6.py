# Write a Python program to:
# Take a number from the user
# Check whether the number is a Palindrome or not
# Example 1
# Input:
# 121
# Output:
# Palindrome
# Example 2
# Input:
# 123
# Output:
# Not Palindrome
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))
original_n = n
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10

if original_n == reversed_n:
    print("Palindrome")
else:
    print("Not Palindrome")