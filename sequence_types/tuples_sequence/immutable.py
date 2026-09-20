"""
This progam Create a tuple: `(10, 20, 30)`  
Try to change the first element to `100`.  
Write a comment explaining why it fails.
"""


numbers = (10, 20, 30)

numbers[0] = 100


"""
This will results to an error because Tuples are Immutable, meaning you cannot
change the tuple onces it created.
"""
