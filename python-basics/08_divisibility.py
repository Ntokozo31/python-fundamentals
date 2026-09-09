"""
This program asks user for a number and checks
if it's divisible by 3 and 5
"""

number = int(input("Please enter your number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Your number is divisible by 3 and 5.")
else:
    print("Your number is not divisible by 3 and 5.")