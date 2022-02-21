from ramda import equals


def test_equals_nocurry():
    assert equals("foo", "foo")


def test_equals_curry():
    assert equals("foo")("foo")
