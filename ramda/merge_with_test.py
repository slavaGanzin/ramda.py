from ramda import *
from ramda.private.asserts import *


def merge_with_test():
    assert_equal(
        merge_with(
            concat, {"a": True, "values": [10, 20]}, {"b": True, "values": [15, 35]}
        ),
        {"a": True, "b": True, "values": [10, 20, 15, 35]},
    )
