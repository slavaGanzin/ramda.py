from .curry import curry
from .complement import complement
from .filter import filter


@curry
def reject(p, xs):
    """The complement of filter.
    Acts as a transducer if a transformer is given in list position. Filterable
    objects include plain objects or any object that has a filter method such
    as Array"""
    return filter(complement(p), xs)
