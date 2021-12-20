from .gte import gte


def gte_test():
    assert gte(3, 2)
    assert not gte(2, 3)
    assert gte(3, 3)
