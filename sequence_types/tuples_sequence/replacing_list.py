"""
This program has broken code (TypeError) and fixed code
successfully change the contents of the list (without replacing the whole list).
"""

# Broken code
t = (1, 2, [3, 4])
t[2] = [5, 6]
print(t)

# Fixed code
t = (1, 2, [3, 4])
t[2][0] = [5, 6]
print(t)