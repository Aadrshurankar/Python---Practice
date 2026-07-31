# Write a Python program to:
# Create a set {10, 20, 30}
# Add multiple values 40 and 50 using a set method
# Print the updated set
# Expected Output:
# {40, 10, 50, 20, 30}

s = {10, 20, 30}
s.update([40, 50])
print(s)