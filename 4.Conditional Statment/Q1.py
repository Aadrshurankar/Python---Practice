# Write a Python program to:
# Take a number from user
# If number is divisible by 2 and 7, print:
# Divisible by 2 and 7
# Else if divisible by 2 only, print:
# Divisible by 2
# Else if divisible by 7 only, print:
# Divisible by 7
# Else print:
# Not divisible by 2 or 7

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 7 == 0:
    print("Divisible by 2 and 7")
elif number % 2 == 0:
    print("Divisible by 2")
elif number % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 2 or 7")