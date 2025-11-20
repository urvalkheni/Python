"""16_exceptions.py
Try/except/finally example.
"""

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Division succeeded")
        return result
    finally:
        print("Operation attempted")

print(safe_divide(10, 2))
print(safe_divide(5, 0))

try:
    raise ValueError("Custom error example")
except ValueError as e:
    print("Caught:", e)
