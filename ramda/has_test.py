from ramda.has import has
from ramda.private.asserts import *


def has_curry_test():
    has_name = has('name')
    assert_equal(has_name({'name': 'alice'}), True)
    assert_equal(has_name({'name': 'bob'}), True)
    assert_equal(has_name({}), False)


def has_nocurry_test():
    point = {'x': 0, 'y': 0}
    assert_equal(has('x', point), True)
    assert_equal(has('y', point), True)
    assert_equal(has('z', point), False)
