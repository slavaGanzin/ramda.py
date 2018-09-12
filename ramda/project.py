from ramda.curry import curry
from ramda.pick import pick


@curry
def project(selectors, list):
    return [pick(selectors, el) for el in list]
