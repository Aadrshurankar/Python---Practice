# Write a Python program to:
# Take a number (age)
# If age >= 60 → "Senior Citizen"
# Else if age >= 18 → "Adult"
# Else if age >= 10 → "Teenager"
# Else → "Child"

age = int(input("Enter your age: "))

if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
elif age >= 10:
    print("Teenager")
else:
    print("Child")