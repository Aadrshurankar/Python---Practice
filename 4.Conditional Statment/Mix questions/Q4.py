# Write a Python program to:
# Take a number from the user
# If number is divisible by 3 and 5, print:
# FizzBuzz
# Else if divisible by 3 only, print:
# Fizz
# Otherwise if divisible by 5 only, print:
# Buzz
# Else print the number itself
# Example
# Input:
# 15
# Output:
# FizzBuzz
# 👉 Write your code 👨‍💻

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)