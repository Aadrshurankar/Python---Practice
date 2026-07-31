# Write a Python program to:
# Take a number n from the user
# Count how many numbers between 1 and n are divisible by 5
# Example
# Input:
# 20
# Output:
# 4
# Because:
# 5, 10, 15, 20
# are divisible by 5.
# 👉 Write your code 👨‍💻

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if i % 5 == 0:
        count += 1
print(count)