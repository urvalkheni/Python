"""08_type_conversion.py
Type casting and input.
"""

raw = input("Enter a number: ")
try:
    num = float(raw)
except ValueError:
    num = None
print("Converted:", num)

# int(), float(), str()
print(int(5.9))
print(float(5))
print(str(123))
