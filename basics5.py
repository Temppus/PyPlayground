print("-------------DICTS-------------")

d1 = {"key1": 5, "key2": 420}
d2 = dict([("name", "Charlie"), ("age", 35), ("city", "Paris")])  # from tuples
d3 = dict(name="Bob", age=30, city="London")  # weird syntax tbh, kwargs ctor

x = {i: i for i in [1, 2, 3]}
print(x)

d = d1

# Accessors
print(d["key1"])  # (KeyError if key doesn't exist)
print(d.get("key1"))  # (Returns None if key is missing)
print(d.get("not_existing_key"))  # (Returns None if key is missing)
print(d.get("salary", 5000))  # Default value if key is missing

# manipulation
d["key1"] = 100
d["new-key"] = 20
d.update([("x", 2)])  # bulk update from tuple list
d.update({"aaa": 9})  # bulk update from other "dict"
print(d)

# Removal (pop or del)
print(d.pop("aaa"))  # Removes and returns value, KeyError if missing
print(d.pop("hmm", "Default Value"))  # Returns default value if missing
del d["new-key"], d["x"]
print(d)

print(d.keys())
print(d.values())
print(d.items())

# Iterating through items (weird that you need to specify .items())
for k, v in d.items():
    print(k, v)

d3 = {"a": 1, "b": 2}
d4 = {"b": 3, "c": 4}

merged = d3 | d4  # (d4 entries will replace d4 entries if same key)
print(f"Merged dicts {merged}")

# Python's defaultdict is a subclass of the dictionary that automatically assigns a default value for non-existent keys, preventing KeyErrors.
# Default value is 0 for int, "" for strings, etc ...
from collections import defaultdict

dd: dict[str, str] = defaultdict(str)
dd["x"] = "A"
print(dd["x"], dd["y"])

print(bool("Hello"))
print(bool(15))
