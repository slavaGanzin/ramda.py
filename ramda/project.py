from toolz import curry
from ramda.pick import pick


@curry
def project(selectors, list):
    """Reasonable analog to SQL select statement"""
    return [pick(selectors, el) for el in list]
