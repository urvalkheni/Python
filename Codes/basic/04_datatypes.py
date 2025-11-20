"""04_datatypes.py
Show basic built-in types and type().
"""

an_int = 10
a_float = 2.75
a_str = "Sample"
a_bool = False

print(type(an_int))
print(type(a_float))
print(type(a_str))
print(type(a_bool))

# None type
nothing = None
print(type(nothing))

# Container types preview
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)
numbers_set = {1, 2, 3}
person_dict = {"name": "Bob", "age": 25}

print(type(numbers_list), type(numbers_tuple), type(numbers_set), type(person_dict))
