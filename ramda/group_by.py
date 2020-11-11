from toolz import curry


@curry
def group_by(f, xs):
    """Splits a list into sub-lists stored in an object, based on the result of
    calling a String-returning function on each element, and grouping the
    results according to values returned.
    Dispatches to the groupBy method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    acc = {}
    for x in xs:
        key = f(x)
        try:
            acc[key].append(x)
        except KeyError:
            acc[key] = [x]

    return acc
