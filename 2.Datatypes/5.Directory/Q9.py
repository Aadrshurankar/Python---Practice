# Write a Python program to:
# Create a dictionary {"name": "Aadrsh", "age": 22}
# Remove the key "age" using a dictionary method
# Print the updated dictionary
# Expected Output:
# {'name': 'Aadrsh'}

d = {"name": "Aadrsh", "age": 22}
d.pop("age")
print(d)