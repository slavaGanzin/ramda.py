from ramda import all


def positive(x):
    return x > 0


def test_all_satisfy_nocurry():
    assert all(positive, [1, 2, 3])
    assert not all(positive, [1, -2, 3])


def test_all_satisfy_curry():
    assert all(positive)([1, 2, 3])
    assert not all(positive)([1, -2, 3])
