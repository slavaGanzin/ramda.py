from ramda import any


def positive(x):
    return x > 0


def test_any_satisfy_nocurry():
    assert any(positive, [-1, -2, 3])
    assert not any(positive, [-1, -2, -3])


def test_any_satisfy_curry():
    assert any(positive)([-1, -2, 3])
    assert not any(positive)([-1, -2, -3])
