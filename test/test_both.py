from ramda import both


def positive(x):
    return x > 0


def less_than_ten(x):
    return x < 10


def test_both_nocurry():
    assert both(positive, less_than_ten, 5)
    assert not both(positive, less_than_ten, 10)
    assert not both(positive, less_than_ten, 0)


def test_both_curry():
    between_zero_and_ten = both(positive, less_than_ten)
    assert between_zero_and_ten(5)
    assert not between_zero_and_ten(10)
    assert not between_zero_and_ten(0)
