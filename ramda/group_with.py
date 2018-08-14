from ramda.curry import curry


@curry
def group_with(predicate, xs):
    out = []
    is_str = isinstance(xs, str)
    group = [xs[0]]

    for x in xs[1:]:
        if predicate(group[-1], x):
            group += [x]
        else:
            out.append(''.join(group) if is_str else group)
            group = [x]

    out.append(''.join(group) if is_str else group)

    return out