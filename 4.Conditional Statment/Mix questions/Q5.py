# Write a Python program to:
# Take a marks value from the user (0–100)
# If marks are 90 or above, print:
# A Grade
# Else if marks are 75 or above, print:
# B Grade
# Else if marks are 50 or above, print:
# C Grade
# Otherwise print:
# Fail
# Example
# Input:
# 80
# Output:
# B Grade
# 👉 Write your code 👨‍💻

marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")