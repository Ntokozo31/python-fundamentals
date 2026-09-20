"""
This program has broken code of indexing error and
second code (fixed indexing error)
"""


# Broken code
t = (5, 10, 15, 20)
print(t[4])
print("Length:", len(t))

# Fixed code
t = (5, 10, 15, 20)
print(f"Last element: {t[-1]}")
print(f"Length: {len(t)}")