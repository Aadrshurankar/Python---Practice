# Write a Python program to:
# Take a number from the user
# Reverse the number using a while loop
# Example
# Input:
# 1234
# Output:
# 4321
# 👉 Write your code 👨‍💻

num = int(input("Enter a number: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("Reversed number:", reverse_num)