from ramda.path_or import path_or
from ramda.private.asserts import *


def path_or_test():
    assert_equal(path_or('N/A', ['a', 'b'], {'a': {'b': 2}}), 2)
    assert_equal(path_or('N/A', ['a', 'b'], {'c': {'b': 2}}), "N/A")