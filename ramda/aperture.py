from ramda.curry import curry


@curry
def aperture(n, xs):
    """ https://ramdajs.com/docs/#aperture """

    if n > len(xs):
        return []

    return [xs[i:i + n] for i in range(0, len(xs), n)]
