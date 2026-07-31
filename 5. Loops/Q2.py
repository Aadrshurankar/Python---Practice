# 🔥 Super Challenge (Interview Favorite)
# Write a Python program to:
# Take a number from the user
# Find the second largest digit in the number
# Example
# Input:
# 58392
# Output:
# 8
# Because:
# Digits = 5, 8, 3, 9, 2
# Largest = 9
# Second Largest = 8

n = int (input("Enter a number: "))

largest = -1
second_largest = -1

while n > 0:
    digit = n % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif largest > digit > second_largest:
        second_largest = digit
    n //= 10

print("The second largest digit is:", second_largest)