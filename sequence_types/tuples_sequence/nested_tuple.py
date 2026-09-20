"""
This program create a nested tuple:  
`(1, [True, False], (3, 4))`  
Print the third element and its type.
"""

nested = (1, [True, False], (3, 4))

print(f"Third element: {nested[2]}")
print(type(nested[2]))