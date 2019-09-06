from .values import values
from ramda.private.asserts import assert_iterables_equal


test_dict = {"a": 1, "b": 2, "c": 3}


def values_test():
    assert_iterables_equal(values(test_dict), [1, 2, 3])
