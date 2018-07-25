from ramda.curry import curry
import builtins


@curry
def min(xs):
    return builtins.min(xs)
