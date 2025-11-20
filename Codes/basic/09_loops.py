"""09_loops.py
for loop, while loop, break, continue.
"""

# For loop
for i in range(5):
    if i == 3:
        continue
    print("i:", i)

# While loop
count = 0
while count < 3:
    print("count:", count)
    count += 1

# Break example
for n in range(10):
    if n == 4:
        print("Breaking at", n)
        break
