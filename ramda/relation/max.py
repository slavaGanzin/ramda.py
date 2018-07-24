from ramda.function.curry import curry
import builtins


@curry
def max(xs):
    return builtins.max(xs)
