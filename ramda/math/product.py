from ramda.function.curry import curry
from ramda.iterable.reduce import reduce
from .multiply import multiply


product = reduce(multiply, 1)
