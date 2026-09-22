"""
This program fix broken code that has indexError
first code (indexError) second code (fixed indexError)
"""


# Broken code
s = "Python"
print(s[6])
print("Length:", len(s))

# Fixed code 
s = "Python"
print(s[-1])
print("Length:", len(s))