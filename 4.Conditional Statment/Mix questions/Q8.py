# Write a Python program to:
# Take a character from the user
# If character is vowel (a, e, i, o, u) → print:
# Vowel
# Else if character is a digit (0-9) → print:
# Digit
# Else → print:
# Special Character
# Example
# Input:
# a
# Output:
# Vowel
# # 👉 Write your code 👨‍💻

# Take a character from the user
char = input("Enter a character: ")
if char in "aeiou":
    print("Vowel")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")