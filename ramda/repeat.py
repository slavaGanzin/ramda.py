from toolz import curry


def repeat(value, times):
    """Returns a fixed list of size n containing a specified identical value"""
    return [value for i in range(0, times)]
