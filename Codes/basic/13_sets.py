"""13_sets.py
Sets: unique elements, union, intersection.
"""

a = {1, 2, 3, 3}
b = {3, 4, 5}
print(a)
print(a | b)
print(a & b)
print(a - b)

a.add(6)
print(a)
