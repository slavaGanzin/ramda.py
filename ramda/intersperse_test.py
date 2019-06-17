from ramda.intersperse import intersperse
from ramda.private.asserts import *


def intesperse_test():
    xs = ["ba", "a", "a"]
    assert_equal(intersperse("n", xs), ["ba", "n", "a", "n", "a"])

    class XS:
        def intersperse(self, separator):
            return [separator for x in xs]

    assert_equal(intersperse("n", XS()), ["n", "n", "n"])
