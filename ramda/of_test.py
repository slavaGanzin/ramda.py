from ramda.private.asserts import *
from ramda.of import of


def of_test():
    assert_equal(of(None), [None])
    assert_equal(of([42]), [[42]])
