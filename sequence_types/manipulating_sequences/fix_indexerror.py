""""
This program has broken code (IndexError) and second code
IndexError is fixed
"""

# Broken code (IndexError)
colours = ["red", "green", "blue"]
#colours[3] = "yellow"
print(colours)

# Fixed code (IndexError)
colours = ["red", "green", "blue"]
colours.extend(["yellow"])
print(colours)