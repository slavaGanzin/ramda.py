from ramda.merge import merge
from ramda.private.asserts import *


def merge_test():
    assert_equal(
        merge({"name": "fred", "age": 10}, {"age": 40}), {"name": "fred", "age": 40}
    )
