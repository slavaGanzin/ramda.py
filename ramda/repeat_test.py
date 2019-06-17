from ramda import *
from ramda.private.asserts import *


def repeat_test():
    assert_equal(repeat("hi", 5), ["hi", "hi", "hi", "hi", "hi"])

    obj = {}
    repeated_objs = repeat(obj, 5)
    assert_equal(repeated_objs, [{}, {}, {}, {}, {}])
    assert_equal(repeated_objs[0], repeated_objs[1])
