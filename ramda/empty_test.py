from .empty import empty


def complement_nocurry_test():
    assert empty('')
    assert empty([])
    assert empty({})
    assert empty(())
    assert not empty((1, 2))
