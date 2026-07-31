# Write a Python program to:
# Take a number n from the user
# Print all numbers from 1 to n
# But:
# If a number is divisible by 3, print "Fizz" instead of the number
# Otherwise print the number
# Example
# Input:
# 10
# Output:
# 1
# 2
# Fizz
# 4
# 5
# Fizz
# 7
# 8
# Fizz
# 10
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)