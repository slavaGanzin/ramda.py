from ramda import *
from ramda.private.asserts import assert_equal


def add10(x):
    return x + 10


def double(x):
    return x * 2


def sub2(x):
    return x - 2


def compose_test():
    composed = compose(sub2, double, add10)
    assert_equal(composed(100), 218)


def compose_multiple_args_test():
    assert_equal(compose(negate, add)(1, 2), -3)


def compose_empty_args_test():
    assert_equal(compose(negate, lambda: 42)(), -42)
