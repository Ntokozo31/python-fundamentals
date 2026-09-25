"""
Create the string `s = "Programming"`.
Using slicing only, print:
- Every second character from the start
- The string reversed
- The last 4 characters in reverse order
"""


s = "Programming"

print(f"Every character from the start: {s[::2]}")
print(f"String reversed: {s[::-1]}")
print(f"Last four characters in reversed order: {s[10:6:-1]}")