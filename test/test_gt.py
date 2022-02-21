from ramda import gt


def test_gt():
    assert gt(3, 2)
    assert not gt(2, 3)
    assert not gt(2, 2)
