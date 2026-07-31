# Write a Python program to:
# Take a character from the user
# If the character is a vowel (a, e, i, o, u), print:
# Vowel
# Otherwise, print:
# Consonant
# Example
# Input:
# e
# Output:
# Vowel
# Write your code 👨‍💻

# Taking input from the user
char = input("Enter a character: ")

# Checking if the character is a vowel
if char in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")