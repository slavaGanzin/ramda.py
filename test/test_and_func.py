from ramda import and_func


def test_and_func():
    assert and_func(True, True)
    assert not and_func(True, False)
    assert not and_func(False, True)
    assert not and_func(False, False)
