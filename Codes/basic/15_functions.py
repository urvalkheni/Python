"""15_functions.py
Defining and calling functions.
"""

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print(greet("Urval"))
print(greet("Shawn", greeting="Hi"))

def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))
