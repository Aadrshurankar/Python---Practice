# Write a Python program to:
# Take a username and password
# Conditions:
# If username = "admin" AND password = "1234" → print:
# Login Successful
# If username is correct but password wrong → print:
# Wrong Password
# Otherwise → print:
# Invalid User
# Example
# Input:
# admin
# 1234
# Output:
# Login Successful
# 👉 Write your code 👨‍💻

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username == "admin":
    print("Wrong Password")
else:
    print("Invalid User")