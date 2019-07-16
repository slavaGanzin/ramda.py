from toolz import curry


@curry
def starts_with(values, list):
    """Checks if a list starts with the provided values"""
    return list[: len(values)] == values
