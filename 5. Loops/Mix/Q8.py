# Write a Python program to:
# Take a number n from the user
# Count the number of digits in that number using while loop
# Example
# Input:
# 12345
# Output:
# 5
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print(count)