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

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
