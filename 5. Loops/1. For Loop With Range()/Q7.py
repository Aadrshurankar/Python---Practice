# Write a Python program to:
# Find the sum of all even numbers from 1 to 20 using for loop
# Expected Output
# 110
# Write your code 👨‍💻

total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
print(total)