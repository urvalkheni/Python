"""15_modules.py
Importing modules.
"""

import math
from math import sqrt

print(math.pi)
print(sqrt(25))

# Import custom function from this folder (if run as a package setup)
from 14_functions import add, greet  # type: ignore
print(add(2, 2))
print(greet("Module"))
