from ramda import complement


def positive(x):
    return x > 0


def test_complement_nocurry():
    assert complement(positive)(0)
    assert complement(positive)(-5)
    assert not complement(positive)(5)


def test_complement_curry():
    nonpositive = complement(positive)
    assert nonpositive(0)
    assert nonpositive(-5)
    assert not nonpositive(5)
