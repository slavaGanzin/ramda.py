from .any import any


def positive(x):
    return x > 0


def any_satisfy_nocurry_test():
    assert any(positive, [-1, -2, 3])
    assert not any(positive, [-1, -2, -3])


def any_satisfy_curry_test():
    assert any(positive)([-1, -2, 3])
    assert not any(positive)([-1, -2, -3])
