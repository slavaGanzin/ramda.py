from ramda.last_index_of import last_index_of
from ramda.private.asserts import *


def last_index_of_test():
    assert_equal(last_index_of(3, [-1, 3, 3, 0, 1, 2, 3, 4]), 6)
    assert_equal(last_index_of(3, [1, 2, 3, 4, 5, 3, 3]), 6)
    assert_equal(last_index_of(10, [1, 2, 3, 4]), -1)
