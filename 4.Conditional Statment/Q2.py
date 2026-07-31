# Write a Python program to:
# Take a character input
# If it is a vowel → print "Vowel"
# Else if it is consonant → print "Consonant"
# Else if it is a digit → print "Digit"
# Else → print "Special Character"

char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print("Vowel")
elif char.isalpha():
    print("Consonant")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")