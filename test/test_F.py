from ramda.F import F


def test_F():
    assert not F(1, 2, 3, 4), "Should be False"
    assert not F(False), "Should be False"
    assert not F(True), "Should be False"
    assert not F({}), "Should be False"
