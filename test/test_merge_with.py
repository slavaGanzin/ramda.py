from ramda import *
from ramda.private.asserts import *


def test_merge_with():
    assert_equal(
        merge_with(
            concat, {"a": True, "values": [10, 20]}, {"b": True, "values": [15, 35]}
        ),
        {"a": True, "b": True, "values": [10, 20, 15, 35]},
    )
