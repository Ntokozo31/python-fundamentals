"""
This program fixes first code (IndexError) and second code fixed
(IndexError)
"""

# Broken code
numbers = [10, 20, 30, 40, 50]
print(numbers[1:10])
print(numbers[10])

# Fixed code
numbers = [10, 20, 30, 40, 50]
print(numbers[1:10])
print(numbers[-1])