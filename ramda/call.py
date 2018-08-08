from ramda.curry import curry


def call(f, *args):
    if (len(args) > 1):
        return f(*args)

    return lambda *args: f(*args)
