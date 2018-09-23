from ramda import *
from ramda.private.asserts import *


def until_test():
    assert_equal(until(lt(100), multiply(2))(1), 128)
