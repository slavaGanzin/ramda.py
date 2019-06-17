from ramda.path_satisfies import path_satisfies
from ramda.private.asserts import *


def path_satisfies_test():
    assert_equal(path_satisfies(lambda y: y > 0, ["x", "y"], {"x": {"y": 2}}), True)

    assert_equal(path_satisfies(lambda y: y == 0, ["b", "z"], {"a": {"x": 2}}), False)
