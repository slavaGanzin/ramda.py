from ramda import any_pass


def positive(x):
    return x > 0


def negative(x):
    return x < 0


def test_any_pass_nocurry():
    assert not any_pass([], "foo")
    assert any_pass([positive, negative], 5)
    assert any_pass([positive, negative], -5)
    assert not any_pass([positive, negative], 0)


def test_any_pass_curry():
    nonzero = any_pass([positive, negative])
    assert nonzero(5)
    assert nonzero(-5)
    assert not nonzero(0)
