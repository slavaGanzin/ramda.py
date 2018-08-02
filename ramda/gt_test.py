from .gt import gt


def gt_test():
    assert gt(2, 3)
    assert not gt(3, 2)
    assert not gt(2, 2)
