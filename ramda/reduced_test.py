from ramda import *
from ramda.private.asserts import *


def reducer(acc, item):
    if item > 3:
        return reduced(acc)

    acc.append(item)
    return acc


def reduced_test():
    assert_equal(reduce(reducer, [], [1, 2, 3, 4, 5]), [1, 2, 3])
