from ramda import *
from ramda.private.asserts import *


def add10(x):
    return x + 10


def double(x):
    return x * 2


def sub2(x):
    return x - 2


piped = pipe(sub2, double, add10)


def test_pipe():
    assert_equal(piped(100), (100 - 2) * 2 + 10)


def test_compose_multiple_args():
    assert_equal(pipe(add, negate)(1, 2), -3)


def test_compose_empty_args():
    assert_equal(pipe(lambda: 42, negate)(), -42)
