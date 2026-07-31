# Write a Python program to:
# Create two lists:
# a = [1, 2, 3]
# b = a
# Modify list b by adding 4
# Check:
# a is b
# a == b
# Print both results
# Expected Output:
# True
# True

a = [1, 2, 3]
b = a
b.append(4)
print(a is b)  # True
print(a == b)  # True