import collections
from toolz import curry


@curry
def concat(X, Y):
    """Returns the result of concatenating the given lists or strings.
    Note: R.concat expects both arguments to be of the same type,
    unlike the native Array.prototype.concat method. It will throw
    an error if you concat an Array with a non-Array value.
    Dispatches to the concat method of the first argument, if present.
    Can also concatenate two members of a fantasy-land
    compatible semigroup"""
    if isinstance(X, getattr(collections, "abc", collections).Set):
        return X.union(Y)

    if isinstance(Y, getattr(collections, "abc", collections).Set):
        return Y.union(X)

    return X + Y
