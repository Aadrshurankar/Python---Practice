# Write a Python program to:
# Take a month number (1-12) from the user
# If month is 12, 1, or 2, print:
# Winter
# Else if month is 3, 4, or 5, print:
# Summer
# Otherwise, print:
# Rainy/Other Season
# Example
# Input:
# 4
# Output:
# Summer
# Write your code 👨‍💻

month = int(input("Enter a month number (1-12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Summer")
else:
    print("Rainy/Other Season")