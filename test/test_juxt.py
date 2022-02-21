from ramda import juxt
from ramda.private.asserts import assert_equal


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def test_juxt_nocurry():
    assert_equal(juxt([add, sub])(1, 2), [3, -1])
