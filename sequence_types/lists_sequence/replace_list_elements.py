"""
This program Create a list of numbers: `[10, 20, 30, 40, 50]`  
Replace the second item with `99` and the last item with `100`.  
Print the list before and after the changes.
"""

numbers = [10, 20, 30, 40, 50]
print(f"List before changes: {numbers}")

numbers[1] = 99
numbers[len(numbers) - 1] = 100

print(f"List after changes: {numbers}")