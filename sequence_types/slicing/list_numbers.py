"""
This program Create a list of 5 numbers and it  
create a full copy of the list using slicing and print both.
"""


numbers = [5, 10, 15, 20, 25]

copy_list = numbers[:]

print(f"Original list: {numbers}")
print(f"Copy of list: {copy_list}")