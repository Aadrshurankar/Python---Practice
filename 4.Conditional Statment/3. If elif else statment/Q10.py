# Write a Python program to:
# Take a username and password from the user
# If username is "admin" AND password is "1234", print:
# Login Successful
# Otherwise, print:
# Login Failed
# Example
# Input:
# admin
# 1234
# Output:
# Login Successful
# Write your code 👨‍💻

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")