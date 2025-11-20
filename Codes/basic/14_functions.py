"""14_functions.py
Defining and calling functions.
"""

def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message.
    name: person name
    greeting: optional greeting word
    """
    return f"{greeting}, {name}!"

message = greet("Alice")
print(message)
print(greet("Bob", greeting="Hi"))

def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))
