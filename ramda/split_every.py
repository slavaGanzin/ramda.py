from toolz import curry


@curry
def split_every(length, collection):
    """Splits a collection into slices of the specified length"""
    return [
        collection[length * i : length * (i + 1)]
        for i in range(0, round(len(collection) / length + 1))
        if collection[length * i : length * (i + 1)]
    ]
