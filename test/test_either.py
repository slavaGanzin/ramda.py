from ramda import either


def positive(x):
    return x > 0


def negative(x):
    return x < 0


def test_either_nocurry():
    assert either(positive, negative, -5)
    assert either(positive, negative, 5)
    assert not either(positive, negative, 0)


def test_either_curry():
    nonzero = either(positive, negative)
    assert nonzero(-5)
    assert nonzero(5)
    assert not nonzero(0)
