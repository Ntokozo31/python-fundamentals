"""
This program ask user for an integer number
and determine whether it is even or odd.
"""

even_odd = int(input("Please enter your number: "))

if even_odd % 2 == 0:
    print("Your number is Even.")
else:
    print("Your number is odd.")