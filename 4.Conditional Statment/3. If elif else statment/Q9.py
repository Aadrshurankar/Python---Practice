# Write a Python program to:
# Take a percentage from the user
# If percentage is 80 or above, print:
# Distinction
# Else if percentage is 60 or above, print:
# First Class
# Else if percentage is 35 or above, print:
# Pass
# Otherwise, print:
# Fail
# Example
# Input:
# 65
# Output:
# First Class
# Write your code 👨‍💻

percentage = float(input("Enter your percentage: "))
if percentage >= 80:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")