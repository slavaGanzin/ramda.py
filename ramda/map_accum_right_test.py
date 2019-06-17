from ramda import *
from ramda.private.asserts import *

digits = ["1", "2", "3", "4"]


def appender(a, b):
    return [a + b, a + b]


def map_accum_test():
    assert_equal(
        map_accum_right(appender, "5", digits),
        [["12345", "2345", "345", "45"], "12345"],
    )
