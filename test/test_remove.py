from ramda import *
from ramda.private.asserts import *


def test_remove():
    assert_equal(remove(2, 3, [1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 6, 7, 8])
