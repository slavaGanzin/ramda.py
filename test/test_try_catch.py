from ramda import *
from ramda.private.asserts import *


def test_try_catch():
    assert_equal(try_catch(lambda x: x["x"], F)({"x": True}), True)
    assert_equal(try_catch(lambda x: x["x"], F)(None), False)
    try_catch(lambda: raise_(Exception("foo")), always("caught"))("bar")
