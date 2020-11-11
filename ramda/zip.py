from toolz import curry


@curry
def zip(first, second):
    """Creates a new list out of the two supplied by pairing up equally-positioned
    items from both lists. The returned list is truncated to the length of the
    shorter of the two input lists.
    Note: zip is equivalent to zipWith(function(a, b) { return [a, b] })"""
    return [[v, second[i]] for i, v in enumerate(first)]
