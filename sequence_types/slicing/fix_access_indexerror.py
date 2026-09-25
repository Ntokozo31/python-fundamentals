"""
This program has IndexError in frst code and fixes
it in second code
"""


# Broken code
s = "Python"
print(s[:100])
print(s[100])

# Fixed code
s = "Python"
print(s[:100])
print(s[1])