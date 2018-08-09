from ramda.curry import curry
from ramda.n_ary import n_ary


@curry
def curry_n(n, f):
    return curry(n_ary(n, f))
