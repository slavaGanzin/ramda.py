from ramda import *
from ramda.private.asserts import *


truncate = when(compose(lt(10), length), pipe(take(10), append("…"), join("")))


def when_test():
    assert_equal(truncate("12345"), "12345")
    assert_equal(truncate("0123456789ABC"), "0123456789…")
