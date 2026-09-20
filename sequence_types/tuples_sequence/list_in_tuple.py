"""
This program Create a tuple that contains a list:  
`(10, 20, [True, True])`  
Change the second item **inside the list** to `False`.  
Print the tuple before and after the change.
"""

mixed = (10, 20, [True, True])

# Before changes
print(f"Before tuple changes: {mixed}")

mixed[2][1] = False

# After changes
print(f"After changes: {mixed}")