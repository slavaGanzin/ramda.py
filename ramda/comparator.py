def comparator(predicate):
    """Makes a comparator function out of a function that reports whether the first
    element is less than the second"""
    return lambda a, b: predicate(a, b) * -1 + predicate(b, a) * 1
