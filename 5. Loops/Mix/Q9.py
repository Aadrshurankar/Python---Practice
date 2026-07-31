# Write a Python program to:
# Take a number n from the user
# Check whether the number is an Armstrong Number or not
# Example 1
# Input:
# 153
# Output:
# Armstrong Number
# Because:
# 1³ + 5³ + 3³ = 153
# Example 2
# Input:
# 123
# Output:
# Not Armstrong Number
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))

original_n = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10

if total == original_n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")