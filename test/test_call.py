from ramda.call import call
from ramda.add import add
from ramda.private import *


def test_call_curry():
    assert_equal(call(add)(1, 2), 3)


def test_call_nocurry():
    assert_equal(call(add, 1, 2), 3)
