from ramda.memoize_with import memoize_with


def once(f):
    return memoize_with(lambda *args: True, f)
