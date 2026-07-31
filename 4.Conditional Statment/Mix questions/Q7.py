# Write a Python program to:
# Take a number from the user
# If number is greater than 0, check:
# If even → print "Positive Even"
# If odd → print "Positive Odd"
# Else if number is less than 0, print:
# "Negative Number"
# Else print:
# "Zero"
# Example
# Input:
# 6
# Output:
# Positive Even
# # 👉 Write your code 👨‍💻

number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")