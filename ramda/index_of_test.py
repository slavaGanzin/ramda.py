from ramda.index_of import index_of
from ramda.private.asserts import *


def index_of_test():
    assert_equal(index_of(3, [1, 2, 3, 4]), 2)
    assert_equal(index_of(10, [1, 2, 3, 4]), -1)
