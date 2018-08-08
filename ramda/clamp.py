from ramda.curry import curry


@curry
def clamp(min, max, value):
    if max < min:
        raise ValueError('\
        min must not be greater than max in clamp(min, max, value)')

    if value > max:
        return max
    if value < min:
        return min
    return value
