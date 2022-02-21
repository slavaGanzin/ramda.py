from ramda import lt


def test_lt():
    assert lt(2, 3)
    assert not lt(3, 2)
    assert not lt(3, 3)
