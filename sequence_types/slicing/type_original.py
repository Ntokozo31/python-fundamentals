"""
This program Create a tuple and a list with the same numbers.  
Slice the first 3 elements from both and print 
the type of each result to prove the slice keeps the original type.
"""


tuple_numbers = (10, 20, 30, 40, 50, 60)

list_numbers = [10, 20, 30, 40, 50, 60]

print(f"First 3 of Tuple: {type(tuple_numbers[:3])}")
print(f"First 3 of List: {type(list_numbers[:3])}")
