# general data types
"""
Text Type:	str
Boolean Type:	bool
Numeric Types:	int, float, complex (complex numbers)

Sequence Types:	list, tuple, range

Mapping Type:	dict
Set Types:	set, frozenset

Binary Types:	bytes, bytearray, memoryview

None Type:	NoneType
"""

a = "Hello, World!"
print(a[1])

print("-------------BOOLEANS-------------")

# Falsy values in Python: False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dictionary), set(), (), and range(0).
# Everything else is truthy.
print(
    bool(0), bool(False), bool(None), bool(0.0), bool(""), bool([]), bool({}), bool(())
)
print(bool("Hello"), bool(15), bool(-1.0))

print("-------------TUPLES-------------")

# tuples ...
my_tuple_a = (1, 2, 3, 4)
my_tuple_b = 1, 2, 3, 4  # tuple packing
print(my_tuple_a)
print(my_tuple_b)

single_element = (5,)  # Correct
not_a_tuple = 5  # This is just an int

print(type(single_element))  # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>

t = tuple([1, 2, 3, 4, 5])  # Converts a list to a tuple

print(t[0])
print(t[2])
print(t[-1])  # last one

# SLICING -> works also for any collection like data type
print(t[1:4])  # (2, 3, 4)
print(t[:3])  # (1, 2, 3)
print(t[::2])  # (1, 3, 5) (every second element)

# tuple unpacking
a, b, c, *rest = t
print(a, b, c, rest)  # rest will be list of rest values in tuple

first_two, *remaining = t[:2], t[2:]  # Using slicing
print(
    first_two,  # tuple of 2
    remaining,
)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found