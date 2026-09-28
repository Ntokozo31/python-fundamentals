"""
This program frst use `append(["a", "b"])` and print the result.  
Then create the list again and use `extend(["a", "b"])` instead.  
Print both results and write a short comment explaining the difference.
"""


numbers = [1, 2, 3]
new_numbers_list = [4, 5, 6]

numbers.append(["a", "b"])
print(numbers)

new_numbers_list.extend(["a", "b"])
print(new_numbers_list)

# Comment
"""
The append method it appends an element as a single element
but the extend method it separetes them as 2 elements, as we see
when we run code the append method give us 4 elements whereas the
extend method gives us 5 elements that also shows us the append method
only gives us the appended items as one but extend gives us the
extended items as 2 or more elements.
"""