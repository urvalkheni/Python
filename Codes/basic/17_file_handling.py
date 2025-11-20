"""17_file_handling.py
Reading and writing files using 'with'.
"""

filename = "sample.txt"

# Write
with open(filename, "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Read
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
print("File content:\n", content)
