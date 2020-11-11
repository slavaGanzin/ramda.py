from toolz import curry


@curry
def without(xs1, xs2):
    """Returns a new list without values in the first argument.
    R.equals is used to determine equality.
    Acts as a transducer if a transformer is given in list position"""
    # TODO: fix implementation
    return [x for x in xs2 if x not in xs1]
