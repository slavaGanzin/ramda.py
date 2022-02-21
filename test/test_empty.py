from ramda import empty


def test_complement_nocurry():
    assert empty("")
    assert empty([])
    assert empty({})
    assert empty(())
    assert not empty((1, 2))
