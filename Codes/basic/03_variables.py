"""03_variables.py
Variables and naming rules.
"""

# Naming rules:
# - lowercase_with_underscores preferred
# - cannot start with a number
# - avoid reserved keywords (if, for, class, etc.)
# - descriptive > short

age = 30
pi = 3.14159
user_name = "Alice"
is_active = True

print(age, type(age))
print(pi, type(pi))
print(user_name, type(user_name))
print(is_active, type(is_active))

# Reassignment (dynamic typing)
age = "thirty"
print(age, type(age))
