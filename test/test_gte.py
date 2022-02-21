from ramda import gte


def test_gte():
    assert gte(3, 2)
    assert not gte(2, 3)
    assert gte(3, 3)
