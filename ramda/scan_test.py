from ramda import *
from ramda.private.asserts import *


def scan_test():
    assert_equal(scan(multiply, 1, [1, 2, 3, 4]), [1, 1, 2, 6, 24])
