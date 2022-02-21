from ramda.index_by import index_by
from ramda.prop import prop
from ramda.private.asserts import *


def test_index_by():
    list = [{"id": "xyz", "title": "A"}, {"id": "abc", "title": "B"}]
    out = {"abc": {"id": "abc", "title": "B"}, "xyz": {"id": "xyz", "title": "A"}}
    assert_equal(index_by(prop("id"), list), out)
