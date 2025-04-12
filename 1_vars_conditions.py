# no new line
print("PYTHON ", end="")
print("BASICS")

# this is kind of hack for multiline comments
mlc = """
Comment Line 1
Comment Line 2
...
"""

# but can be actually assignable to variable :D
print(mlc)

# vars + optional explicit casting
int_var = int(10)
float_var = float(9)
str_var = str(8)

# conditional logical operators
a = int_var > 0 and int_var < 10
b = int_var > 0 or int_var < 10
c = not (int_var > 0 or int_var < 10)
print(a, b, c)

# conditions
five = 5
ten = 10

if five > ten:
    print("x is > y")
elif five < ten:
    print("x is < y")
else:
    print("x is == y")  # can also be on same line

# Ternary operators (pretty weird design choice tbh)
print("BIGGER") if five > ten else print("LOWER")

# lol why would I wanted to do nothing in if clause, but if you need you can pass :D
# pass can be used also for empty body function
if five > ten:
    pass

print("-------------TYPES-------------")
print(type(int_var))
print(type(float_var))
print(type(str_var))


print("------------- VALUES-------------")
print(int_var + 3)
print(float_var + 3)
print(
    str_var + "3"
)  # simple 3 would be TypeError: can only concatenate str (not "int") to str

# same value for multiple vars
x = y = z = "Orange"

# one liner for multiple const values
x, y, z = "Orange", "Banana", "Cherry"

# array unpacking to vars
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# print multiple values
print(x, y, z, 5, "John")