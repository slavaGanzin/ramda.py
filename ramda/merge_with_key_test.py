from ramda import *
from ramda.private.asserts import *


def concat_values(k, l, r):
    return concat(l, r) if k == "values" else r


def merge_with_key_test():
    assert_equal(
        merge_with_key(
            concat_values,
            {"a": True, "thing": "foo", "values": [10, 20]},
            {"b": True, "thing": "bar", "values": [15, 35]},
        ),
        {"a": True, "b": True, "thing": "bar", "values": [10, 20, 15, 35]},
    )
