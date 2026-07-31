# Write a Python program to:
# Take a number n from the user
# Print numbers from n down to 1
# Do not print numbers that are divisible by 2
# Example
# Input:
# 10
# Output:
# 9
# 7
# 5
# 3
# 1
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i)