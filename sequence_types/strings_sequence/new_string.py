"""
This program fix the problem and fix it by creating a **new** 
string instead of trying to modify the original one.
"""

# Broken code (TypeError)
s = "World"
s[1] = "a"
print(s)

# Fixed code (TyepeError)
s = "World"
s = "warld"
print(s)