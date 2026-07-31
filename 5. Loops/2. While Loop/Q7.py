# 💡 Write a Python program to:
# Find the sum of all even numbers from 2 to 20 using a while loop.
# Expected Output
# 110
# 👉 Write your code 👨‍💻

sum_even = 0
num = 2

while num <= 20:
    sum_even += num
    num += 2

print(sum_even)