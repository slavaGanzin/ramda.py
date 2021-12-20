from .lte import lte


def lte_test():
    assert lte(2, 3)
    assert not lte(3, 2)
    assert lte(3, 3)
