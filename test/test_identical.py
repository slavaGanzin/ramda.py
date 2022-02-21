from ramda import identical


def test_identical_nocurry():
    assert identical(1, 1)
    assert not identical([1], [1])


def test_identical_curry():
    assert identical(1)(1)
    assert not identical([1])([1])
