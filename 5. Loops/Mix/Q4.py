# Write a Python program to:
# Take a number n from the user
# Find the sum of digits of that number using a loop
# Example
# Input:
# 1234
# Output:
# 10
# Because:
# 1 + 2 + 3 + 4 = 10
# 👉 Write your code 👨‍💻

n = int(input("Enter a no: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print(total)