from toolz import curry


@curry
def filter(p, xs):
    """Takes a predicate and a Filterable, and returns a new filterable of the
    same type containing the members of the given filterable which satisfy the
    given predicate. Filterable objects include plain objects or any object
    that has a filter method such as Array.
    Dispatches to the filter method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    if not hasattr(xs, "__iter__"):
        return []

    if hasattr(xs, "values"):
        out = {}
        for k, v in xs.items():
            if p(v):
                out[k] = v
        return out

    return [x for x in xs if p(x)]
