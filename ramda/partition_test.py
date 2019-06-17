from ramda.partition import partition
from ramda.contains import contains
from ramda.private.asserts import *


def partition_test():
    assert_equal(
        partition(contains("s"), ["sss", "ttt", "foo", "bars"]),
        [["sss", "bars"], ["ttt", "foo"]],
    )

    assert_equal(
        partition(contains("s"), {"a": "sss", "b": "ttt", "foo": "bars"}),
        [{"a": "sss", "foo": "bars"}, {"b": "ttt"}],
    )
