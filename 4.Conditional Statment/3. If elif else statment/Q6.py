# Write a Python program to:
# Take a character from the user
# If the character is 'A', print:
# Excellent
# Else if the character is 'B', print:
# Good
# Otherwise, print:
# Needs Improvement
# Example
# Input:
# B
# Output:
# Good
# Write your code 👨‍💻

# Take a character from the user
character = input("Enter a character: ")
# Check the character and print the appropriate message
if character == 'A':
    print("Excellent")
elif character == 'B':
    print("Good")
else:
    print("Needs Improvement")