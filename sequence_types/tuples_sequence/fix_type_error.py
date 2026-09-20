"""
This program has type error broken code and it fixed broken on the
second code.
"""


# Broken code
t = (10, 20, 30)
t[0] = 100
print(t)

# Fixed broken code
t = (10, 20, 30)
print(f"First elment: {t[0]}")
