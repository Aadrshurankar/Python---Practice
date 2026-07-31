# 🔥 Ultimate Loop Challenge
# Take a number from the user and find the frequency of digit 5.
# Example
# Input:
# 155525
# Output:
# 4
# Because digit 5 appears 4 times.

n = int (input("Enter a number: "))
count = 0

while n > 0:
    digit = n % 10
    if digit == 5:
        count += 1
    n //= 10
print("Frequency of digit 5:", count)