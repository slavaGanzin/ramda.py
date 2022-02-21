from ramda.private.asserts import *
from ramda.of import of


def test_of():
    assert_equal(of(None), [None])
    assert_equal(of([42]), [[42]])
