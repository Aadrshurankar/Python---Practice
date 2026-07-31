# Write a Python program to:
# Take marks from user (0–100)
# If marks >= 90 → "A"
# Else if marks >= 80 → "B"
# Else if marks >= 70 → "C"
# Else if marks >= 60 → "D"
# Else → "Fail"

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Fail")