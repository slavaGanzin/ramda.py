def ascend(predicate):
    """Makes an ascending comparator function out of a function that returns a value
    that can be compared with < and >"""

    def comparator(a, b):
        _a, _b = predicate(a), predicate(b)
        return (_a < _b) * -1 + (_a > _b) * 1

    return comparator
