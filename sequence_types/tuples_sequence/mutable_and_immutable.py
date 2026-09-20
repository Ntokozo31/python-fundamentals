"""
This program Explains (as comments in the code) the difference between:
- Changing an element of the tuple itself
- Changing an element inside a list that is stored in the tuple
"""

"""
You cannot change an element of the tuple itself coz
tuples are immutable, so after having elements of tuples itself
you cannot change them it will results to TypeError.
"""

# Example
numbers = (10, 20, 30, 40, 100)

numbers[-1] = 50


"""
You can change a list element that is sorted in the tuple
because you are changing a sequence that is mutable, that change will
not results to an error because list is mutable.
"""

# Example
mixed = (10, 20, ["Bob", "Dube"], (30, 40))

mixed[2][0] = "Ntokozo"

print(mixed)