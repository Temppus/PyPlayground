# global variable
glob_var = 9

print("-------------GLOBAL VARS-------------")


def add_func_accessing_global_var(addition):
    # to access global variable it must states explicitly, otherwise local one will be used
    global glob_var
    print(f"glob var is {glob_var}")
    glob_var += addition
    print(f"glob var is {glob_var}")
    return None  # "void" (optional)


add_func_accessing_global_var(1)

print(f"glob var after func call {glob_var}")

print("-------------FUNCTIONS-------------")


# func that accept param and returns value
def join_func(num1, num2):
    return str(num1) + str(num2)


# optional typing has no runtime side effect, it is for static type checking only
def join_func_typed(num1: int, num2: int | float) -> str:
    return str(num1) + str(num2)


print(join_func_typed(420, num2=9))


# variable params func
def var_param_func(*params):
    print("Second param is " + params[1])


var_param_func("One", "Two", "Three")


# variable func with possibility to access by param name
def kwargs_func(**variable_args):
    print("Name is " + variable_args["name"])


kwargs_func(name="John", desc="Desc")

print("-------------LAMBDAS-------------")

# lambda arguments: expression
times_two = lambda x: x * 2
print(times_two(7))

print_lambda = lambda x: print(x)
print_lambda(9)

# multiple param lambda
m = lambda a, b, c: a + b + c
print(m(4, 2, 0))


# lambdas can be returned and pass around
def get_lambda(n):
    return lambda a: a * n
