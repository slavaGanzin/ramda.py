from ramda.insert import insert
from ramda.private.asserts import *


def test_insert():
    assert_equal(insert(2, "x", [1, 2, 3, 4]), [1, 2, "x", 3, 4])
