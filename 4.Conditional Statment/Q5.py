# Write a Python program to:
# Take a username and password
# If username = "admin" AND password = "1234" → "Login Success"
# Else if username = "admin" but password wrong → "Wrong Password"
# Else if username is wrong → "Invalid User"
# Else → "Try Again"

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Success")
elif username == "admin" and password != "1234":
    print("Wrong Password")
elif username != "admin":
    print("Invalid User")
else:
    print("Try Again")