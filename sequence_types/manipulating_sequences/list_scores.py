"""
This program replace first 3 scores using
slicing assignment and print list before, after change, new length
of the list
"""


scores = [55, 70, 85, 90, 60, 75]

print(f"List before changes: {scores}")

scores[0:3] = [80, 82, 88]

print(f"List after changes: {scores}")
print(f"length: {len(scores)}")
