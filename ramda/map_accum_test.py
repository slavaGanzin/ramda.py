from ramda import *
from ramda.private.asserts import *

digits = ["1", "2", "3", "4"]


def appender(a, b):
    c = a + b
    return [c, c]


def map_accum_test():
    assert_equal(
        map_accum(appender, "0", digits), ["01234", ["01", "012", "0123", "01234"]]
    )
