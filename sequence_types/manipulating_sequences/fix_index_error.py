"""
This program fix IndexError from the first code,
and prints first element in fixed (second code)
"""

# Broken code
numbers = [5, 10, 15, 20, 25]
del numbers[1:4]
print(numbers[3])

# Fixed code
numbers = [5, 10, 15, 20, 25]
del numbers[1:4]
print(numbers[0])