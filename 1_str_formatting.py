int_var = 1
float_var = float(1)

print("-------------STRING FORMATTING/INTERPOLATION-------------")

# (1) simple nice one
print(f"Int value {int_var} is bigger than float value {float_var}")

# (2) %-formatting
print(
    "Hi name is %s with height %d and age %f or simpler %.1f "
    % ("John Wick Height is", 182, 44.5, 44.50)
)
# not a print specific
test_str = "Hmm %s" % ("hmmmm")
print(test_str)

# (3) string format approach
str_formatted = "Apples to {}".format("Orangs")
print(f"{str_formatted}")