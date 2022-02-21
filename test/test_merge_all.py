from ramda.merge_all import merge_all
from ramda.private.asserts import *


def test_merge_all():
    assert_equal(
        merge_all([{"foo": 1}, {"bar": 2}, {"baz": 3}]), {"foo": 1, "bar": 2, "baz": 3}
    )
    assert_equal(merge_all([{"foo": 1}, {"foo": 2}, {"bar": 2}]), {"foo": 2, "bar": 2})
