"""05_strings.py
String indexing, slicing, methods, f-strings, escapes.
"""

course = "Python Programming"
print(course[0])        # first char
print(course[-1])       # last char
print(course[0:6])      # slice
print(course[:6])       # from start
print(course[7:])       # to end
print(course[:])        # copy whole

# Methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("thon"))
print(course.replace("o", "0"))
print("Python" in course)

# Escape characters
escaped = "Line1\nLine2\tTabbed \"quoted\""
print(escaped)

# f-string
first = "Alice"
last = "Smith"
full = f"{first} {last}"
print(full)
