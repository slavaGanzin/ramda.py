from ramda import contains_with


def pair_equal(pair1, pair2):
    a1, a2 = pair1
    b1, b2 = pair2
    return a1 == b1 and a2 == b2


pairs = [(1, 2), (2, 1), (3, 4)]


def test_contains_with_nocurry():
    assert contains_with(pair_equal, (1, 2), pairs)
    assert not contains_with(pair_equal, (4, 3), pairs)


def test_contains_with_curry():
    contains_pair = contains_with(pair_equal)
    assert contains_pair((1, 2))(pairs)
    assert not contains_pair((4, 3))(pairs)
