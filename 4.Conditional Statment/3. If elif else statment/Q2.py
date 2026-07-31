# Write a Python program to:
# Take a student's marks as input
# If marks are 90 or above, print:
# Grade A
# Else if marks are 75 or above, print:
# Grade B
# Otherwise, print:
# Grade C
# Example
# Input:
# 82
# Output:
# Grade B
# Write your code 👨‍💻

marks = int(input("Enter the student's marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")