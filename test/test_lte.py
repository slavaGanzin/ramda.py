from ramda import lte


def test_lte():
    assert lte(2, 3)
    assert not lte(3, 2)
    assert lte(3, 3)
