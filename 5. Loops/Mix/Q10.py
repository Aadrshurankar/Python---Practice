# Write a Python program to:
# Take a number n from the user
# Print the largest digit present in the number
# Example
# Input:
# 58392
# Output:
# 9
# 👉 Write your code 👨‍💻


n= input("Enter a number: ")

largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print("The largest digit is:", largest)