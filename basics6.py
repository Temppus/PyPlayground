x = 5
y = 10

if x > y:
    print("x is > y")
elif x < y:
    print("x is < y")
else:
    print("x is == y")  # can also be on same line

# Ternary operators (pretty bad design choice tbh)
print("BIGGER") if x > y else print("LOWER")

# lol why would I wanted to do nothing in if clause, but if you need you can pass :D
# pass can be used also for empty body function
if x > y:
    pass

print("-------------LOOPS-------------")

# pretty standard loop as in other langs
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

for x in range(5, 10, 1):  # from 5 to 9, with step of 1
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
        continue
