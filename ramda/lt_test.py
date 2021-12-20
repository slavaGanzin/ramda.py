from .lt import lt


def lt_test():
    assert lt(2, 3)
    assert not lt(3, 2)
    assert not lt(3, 3)
