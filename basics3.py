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

print("-------------LISTS-------------")
# python uses list heavily instead of arrays afaik
my_list = [
    "Apple",
    9,
    False,
    (1, 2, 3),  # tuples (non mutable)
    {"dictKey1": 1, "dictKey2": 2},  # dicts (mutable)
]

print(f"{my_list}")

my_list.append(float(4.20))

# access last element
print(
    f"Last element {my_list[len(my_list) - 1]}"
)  # count of items in any collection is len(list), WTF ? iot is what it is ....
# or like this (preferred)
print(f"Last element {my_list[-1]}")

my_list.insert(0, "inserted at first idx")
my_list.extend(
    ["ext1", "ext2"]
)  # extend -> append all the elements from an iterable (another list, set, etc.) to the list.
my_list = my_list + [555]  # this works also

print(f"JOINED LISTS {my_list}")

print("LIST ITEMS DELETION")
# my_list.remove("not existing") # raise and error
my_list.remove("Apple")  # remove by value
my_list.pop(0)  # remove at idx
del my_list[0], my_list[1]
del my_list[0:1]
print(f"After deletion {my_list}")

print("SHALLOW COPY OF LIST ITEMS")
# shallow copy of elements (will copy only immutable types, mutable types will be refs only)
shallowed_copied_list = my_list.copy()  # or could be list(my_list) also
shallowed_copied_list.append("appended")

print("Comparing shallow copy lists")
print(f"{my_list} VS {shallowed_copied_list}")

# runtime type checking (makes also mypy happy)
if isinstance(shallowed_copied_list[0], dict):
    # this will modify value in dict in both
    # because dict is not immutable data type, so same ref was used when creating shallow copy
    shallowed_copied_list[0]["dictKey1"] = 9999

print(f"{my_list} VS {shallowed_copied_list}")

# removal is independent
shallowed_copied_list.pop(0)
print(f"{my_list} VS {shallowed_copied_list}")

print("SORTING OF LISTS")
s: list[str | int] = ["z", "x", "y"]

# sort  will change underlying order in list
s.sort()
print(f"Sorted list {s}")

# sorted does not modify iterable
print(f"Reverse sorted list via sorted {sorted(s, reverse=True)}")

# filter items that are not "x"
s.append(123)
iterable = filter(
    lambda s: s == "x", s
)  # returns iterable, more on to that in class stuff I guess
print(f"Filtered:{list(iterable)}")
