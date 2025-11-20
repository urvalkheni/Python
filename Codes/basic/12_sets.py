"""12_sets.py
Sets: unique elements, union, intersection.
"""

a = {1, 2, 3, 3}
b = {3, 4, 5}
print(a)  # duplicates removed
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference

a.add(6)
print(a)
