from ramda.call import call
from ramda.add import add
from ramda.private.asserts import *


def call_curry_test():
    assert_equal(call(add)(1, 2), 3)


def call_nocurry_test():
    assert_equal(call(add, 1, 2), 3)
