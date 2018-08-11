from ramda.curry import curry


@curry
def drop_repeats_with(f, xs):
    out = [xs[0]]
    for i in range(0, len(xs) - 1):
        if not f(*xs[i:i + 2]):
            out.append(xs[i + 1])
    return out
