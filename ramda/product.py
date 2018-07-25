from ramda.curry import curry
from ramda.reduce import reduce
from .multiply import multiply


product = reduce(multiply, 1)
