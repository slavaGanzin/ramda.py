from ramda.memoize_with import memoize_with


def once(f):
    """Accepts a function fn and returns a function that guards invocation of
    fn such that fn can only ever be called once, no matter how many times
    the returned function is invoked. The first value calculated is returned in
    subsequent invocations"""
    return memoize_with(lambda *args: True, f)
