# 🔥 Hard Interview Question
# Take a number from the user and find the sum of even digits only.
# Example
# Input:
# 123456
# Output:
# 12
# Because:
# 2 + 4 + 6 = 12

n = int (input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n //= 10

print("The sum of even digits is:", total)