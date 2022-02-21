from ramda import contains


def test_contains_nocurry():
    assert contains(2, [1, 2, 3])
    assert not contains(0, [1, 2, 3])


def test_contains_curry():
    assert contains(2)([1, 2, 3])
    assert not contains(0)([1, 2, 3])
