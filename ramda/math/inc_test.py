from .inc import inc
from ramda.private.asserts import assert_equal


def inc_test():
    assert_equal(inc(5), 6)
