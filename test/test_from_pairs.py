from ramda.from_pairs import from_pairs
from ramda.private.asserts import *


def test_from_pairs():
    assert_equal(from_pairs([["a", 1], ["b", 2], ["c", 3]]), {"a": 1, "b": 2, "c": 3})
