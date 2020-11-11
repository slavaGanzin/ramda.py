from toolz import curry
from ramda.prop_eq import prop_eq


@curry
def where_eq(spec, object):
    """Takes a spec object and a test object; returns true if the test satisfies
    the spec, false otherwise. An object satisfies the spec if, for each of the
    spec's own properties, accessing that property of the object gives the same
    value (in R.equals terms) as accessing that property of the
    spec.
    whereEq is a specialization of where"""
    for k, v in spec.items():
        if not prop_eq(k, v, object):
            return False
    return True
