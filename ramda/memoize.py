import hashlib
import json
from ramda.memoize_with import memoize_with


def memoize(f):
    """Creates a new function that, when invoked, caches the result of calling fn
    for a given argument set and returns the result. Subsequent calls to the
    memoized fn with the same argument set will not result in an additional
    call to fn; instead, the cached result for that set of arguments will be
    returned"""

    def hash(*args):
        return hashlib.sha256(json.dumps(args).encode("utf-8")).hexdigest()

    return memoize_with(hash, f)
