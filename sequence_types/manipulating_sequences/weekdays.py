"""
This program Start with:  
`["Monday", "Wednesday", "Friday"]`  

Insert `"Tuesday"` at the correct position so the days are in order.  
Then insert `"Thursday"` at the correct position.  
Print the final list.
"""


days = ["Monday", "Wednesday", "Friday"]

days.insert(1, "Tuesday")
days.insert(3,"Thursday")

print(days)