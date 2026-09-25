"""
This program uses only slice assignment, to replace `"Exercise"` and `"Study"` with three new tasks:  
`"Read"`, `"Code"`, `"Review"`.  
Print the final list and its length.
"""


daily_tasks = ["Wake up", "Exercise", "Study", "Cook", "Sleep"]

daily_tasks[1:3] = ["Exercise", "Study"]

print(f"Final Daily tasks are: {daily_tasks}")
print(f"Length: {len(daily_tasks)}")