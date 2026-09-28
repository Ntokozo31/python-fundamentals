"""
This program Create a list of 6 numbers.  
Delete the first and the last element using two separate `del` statements.  
Print the final list.
"""

numbers = [5, 10, 15, 20, 25, 30]

del numbers[0]
del numbers[-1]

print(numbers)