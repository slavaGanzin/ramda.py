from toolz import curry


@curry
def clamp(min, max, value):
    """Restricts a number to be within a range.
    Also works for other ordered types such as Strings and Dates"""
    if max < min:
        raise ValueError(
            "\
        min must not be greater than max in clamp(min, max, value)"
        )

    if value > max:
        return max
    if value < min:
        return min
    return value
