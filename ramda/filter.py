from ramda.curry import curry


@curry
def filter(p, xs):
    if not hasattr(xs, '__iter__'):
        return []

    if hasattr(xs, 'values'):
        out = {}
        for k, v in xs.items():
            if p(v):
                out[k] = v
        return out

    return [x for x in xs if p(x)]
