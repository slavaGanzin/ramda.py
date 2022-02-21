from ramda.insert_all import insert_all
from ramda.private.asserts import *


def test_insert_all():
    assert_equal(
        insert_all(2, ["x", "y", "z"], [1, 2, 3, 4]), [1, 2, "x", "y", "z", 3, 4]
    )
