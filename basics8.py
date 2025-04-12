try:
    assert "Hi" == "hello"
except AssertionError: 
    print('AssertionError caught ...')


try:
    d = 9 / 0
    print("a")
except ZeroDivisionError:
    print("Div error caught")
finally:
    print("Moving on")


# custom exception definition
# sorry but having class named Exception and calling it Error is weird
class EvenNumberError(Exception):
    pass


def assert_num_is_even(num: int):
    if num % 2 == 0:
        raise EvenNumberError(f"Num {num} is even number")
    return None


# catch and handle our exception
try:
    assert_num_is_even(7)
    assert_num_is_even(8)
except EvenNumberError as e:
    print(f"Handled EvenNumberException with reason {e}")
