# 🔥 BONUS INTERVIEW QUESTION (Harder)
# This is commonly asked in interviews.
# Question
# Take a number from the user and find the smallest digit present in the number.
# Example
# Input:
# 58392
# Output:
# 2

n = input("Enter a number: ")

smallest = 9

while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print("The smallest digit is:", smallest)