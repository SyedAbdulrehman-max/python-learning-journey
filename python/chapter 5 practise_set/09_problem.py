'''QNO9:
Can you change the values inside a list which is contained 
in set S?
s={8, 7, 12, "Harry", [1,2]}'''
# You CANNOT put a list inside a set because lists are mutable and unhashable.
# Example (will cause error):
# s = {1, 2, [3, 4]}  # TypeError!

# Instead, use a tuple (which is immutable):
s = {1, 2, (3, 4)}  # This works fine
print(s)
