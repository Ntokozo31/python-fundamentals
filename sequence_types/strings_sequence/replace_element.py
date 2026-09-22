"""
This program Create a string `"Hello"`.  
tries to change the first character to `"J"`.  
and write a comment explaining why it fails.
"""


greet = "Hello"

greet[0] = "J"

"""
You cannot change element in a string once it has been created because strings
are Immutable (cannot change it), if you try change it python will raise
TypeError because strings are Immutable.
"""