from ramda import *
from ramda.private.asserts import *


def test_uniq_by():
    assert_equal(uniq_by(abs, [-1, -5, 2, 10, 1, 2]), [-1, -5, 2, 10])
    assert_equal(
        uniq_by(abs, {-1, -5, 2, 10, 1, 2}),
        [
            1,
            2,
            10,
            -5,
        ],
    )
