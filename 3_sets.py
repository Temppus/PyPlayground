# set is unordered collection that does not allow duplicate values
s = {1, 2, 3, 4}
s = set([1, 2, 3, 4])  # or this

print(2 in s)  # True
print(10 not in s)  # True

s.add(5)  # adds single an element
s.update([6, 7, 8, 9, 10])  # adds multiple elements
s.remove(3)  # Removes an element (raises KeyError if not found)
s.discard(420)  # Removes an element (does NOT raise error if not found)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # "Symmetric Difference"
# aka (get elements from both sets except their common elements) {1, 2, 4, 5}

print({1, 2, 3} == {3, 1, 2})  # True (Order doesn't matter)
print({1, 2} < {1, 2, 3})  # True (is subset)

# frozenset (for readonly readonly efficient reading)
frozenset(s)
print(s)
