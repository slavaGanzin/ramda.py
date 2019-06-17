from ramda import *
from ramda.private.asserts import *


def zip_test():
    assert_equal(zip([1, 2, 3], ["a", "b", "c", "e"]), [[1, "a"], [2, "b"], [3, "c"]])
