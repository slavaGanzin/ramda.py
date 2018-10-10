from ramda import *
from ramda.private.asserts import *


def uniq_by_test():
    assert_equal(uniq_by(abs, [-1, -5, 2, 10, 1, 2]), [-1, -5, 2, 10])
