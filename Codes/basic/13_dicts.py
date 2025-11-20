"""13_dicts.py
Dictionaries: key:value pairs and methods.
"""

person = {"name": "Alice", "age": 30}
print(person.get("name"))
print(person.get("job", "Not specified"))

person["age"] = 31
person["city"] = "Paris"

print(person.keys())
print(person.items())

for key, value in person.items():
    print(key, "=", value)
