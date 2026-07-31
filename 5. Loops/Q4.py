# 🔥 Interview Challenge (Very Common)
# Take a number from the user and check whether it contains the digit 7.
# Example 1
# Input:
# 12374
# Output:
# Contains 7
# Example 2
# Input:
# 12345
# Output:
# Does Not Contain 7

n = int (input("Enter a number: "))
found = False

while n > 0:
    digit = n % 10
    if digit == 7:
        found = True
        break
    n = n // 10

if found:
    print("Contains 7")
else:    
    print("Does Not Contain 7")