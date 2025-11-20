"""06_numbers.py
Arithmetic operators, augmented assignment, math module.
"""
import math

a = 7
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Augmented assignments
a += 1
a *= 2
print("a now:", a)

# Math functions
value = 3.75
print(round(value))
print(abs(-value))
print(math.floor(value))
print(math.ceil(value))
print(math.sqrt(16))
