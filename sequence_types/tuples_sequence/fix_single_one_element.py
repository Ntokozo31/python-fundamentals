"""
This program currently creates 4 elements in the first code.  
Second code fix it so that `(3, 4)` becomes one single element (a nested tuple).
"""


# Creates 4 elements
t = 1, [True, False], 3, 4
print(len(t))
print(t[2])


# Creates 3 elements
t = (1, [True, False], (3, 4))
print(len(t))
print(t[2])
