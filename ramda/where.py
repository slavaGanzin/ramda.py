from toolz import curry
from ramda.prop import prop


@curry
def where(spec, object):
    """Takes a spec object and a test object; returns true if the test satisfies
    the spec. Each of the spec's own properties must be a predicate function.
    Each predicate is applied to the value of the corresponding property of the
    test object. where returns true if all the predicates return true, false
    otherwise.
    where is well suited to declaratively expressing constraints for other
    functions such as filter and find"""
    for k, f in spec.items():
        if not f(prop(k, object)):
            return False
    return True
