from ramda.private.asserts import *
from ramda.partial import partial


def multiply2(a, b):
    return a * b


def greet(salutation, title, firstName, lastName):
    return salutation + ", " + title + " " + firstName + " " + lastName + "!"


def partial_test():
    double = partial(multiply2, [2])
    assert_equal(double(2), 4)

    say_hello = partial(greet, ["Hello"])
    say_hello_to_ms = partial(say_hello, ["Ms."])

    assert_equal(say_hello_to_ms("Jane", "Jones"), "Hello, Ms. Jane Jones!")
