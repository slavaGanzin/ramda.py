from ramda import or_func


def test_or_func():
    assert or_func(True, True)
    assert or_func(True, False)
    assert or_func(False, True)
    assert not or_func(False, False)
