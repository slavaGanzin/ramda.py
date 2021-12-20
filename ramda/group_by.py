from toolz import curry
from ramda.is_empty import is_empty


@curry
def group_by(f, xs):
    """Splits a list into sub-lists stored in an object, based on the result of
    calling a String-returning function on each element, and grouping the
    results according to values returned.
    Dispatches to the groupBy method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    if is_empty(xs):
        return {}

    acc = {}
    for x in xs:
        key = f(x)
        try:
            acc[key].append(x)
        except KeyError:
            acc[key] = [x]

    return acc
