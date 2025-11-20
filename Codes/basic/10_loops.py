"""10_loops.py
for loop, while loop, break, continue.
"""

for i in range(5):
    if i == 3:
        continue
    print("i:", i)

count = 0
while count < 3:
    print("count:", count)
    count += 1

for n in range(10):
    if n == 4:
        print("Breaking at", n)
        break
