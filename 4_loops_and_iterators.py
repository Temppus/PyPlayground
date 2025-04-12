print("-------------LOOPS-------------")

# pretty standard loop as in other langs
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

for five in range(5, 10, 1):  # from 5 to 9, with step of 1
    if five % 2 == 0:
        print(f"{five} is even")
    else:
        print(f"{five} is odd")
        continue


print("-------------ITERATORS-------------")

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

tuple = ("apple", "banana", "cherry")
tuple_itr = iter(tuple)

# print first and advance iterator
print(next(tuple_itr))

# print rest of iterable
for x in tuple_itr:
    print(x)

# U can make class that implements __iter__() and __next__() and it will be iterable
# But that is niche. U can make stop iteration in this class by raisin StopIteration