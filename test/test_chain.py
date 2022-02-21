from ramda import chain
from ramda.private.asserts import assert_iterables_equal


def to_two(x):
    return [x, x]


def test_chain_nocurry():
    assert_iterables_equal(chain(to_two, [1, 2, 3]), [1, 1, 2, 2, 3, 3])


def test_chain_curry():
    assert_iterables_equal(chain(to_two)([1, 2, 3]), [1, 1, 2, 2, 3, 3])
