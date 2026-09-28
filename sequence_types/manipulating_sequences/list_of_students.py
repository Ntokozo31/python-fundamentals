"""
This program have this list of students:  
`["Thabo", "Lerato", "Sipho", "Naledi", "Kagiso", "Ayanda"]` and it
Remove the middle two students using a single `del` statement.  
Then print how many students remain.
"""

students = ["Thabo", "Lerato", "Sipho", "Naledi", "Kagiso", "Ayanda"]

del students[2:4]

print(f"There are {len(students)} students remaining")