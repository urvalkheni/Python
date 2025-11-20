"""05_operators.py
Demonstrates arithmetic, comparison, logical, assignment,
membership, identity, and a ternary expression.
"""

a = 7
b = 3

# Arithmetic
print("Arithmetic:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Comparison
print("\nComparison:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a <= b:", a <= b)

# Logical
print("\nLogical:")
is_member = True
has_coupon = False
print("is_member and has_coupon:", is_member and has_coupon)
print("is_member or has_coupon:", is_member or has_coupon)
print("not is_member:", not is_member)

# Assignment
print("\nAssignment:")
x = 10
print("x =", x)
x += 5
print("x += 5 ->", x)
x *= 2
print("x *= 2 ->", x)

# Membership
print("\nMembership:")
text = "python"
print("'py' in text:", "py" in text)
print("'java' not in text:", "java" not in text)

# Identity
print("\nIdentity:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

# Ternary (conditional expression)
print("\nTernary operator:")
age = 20
status = "adult" if age >= 18 else "minor"
print("Age:", age, "->", status)
