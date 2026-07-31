# Write a Python program to:
# Take a year from the user
# Check if it is a leap year or not
# Rules:
# A year is leap year if:
# divisible by 400 OR
# divisible by 4 AND not divisible by 100
# Output:
# If leap year → print:
# Leap Year
# Else:
# Not a Leap Year
# Example
# Input:
# 2000
# Output:
# Leap Year
# 👉 Write your code 👨‍💻

year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")