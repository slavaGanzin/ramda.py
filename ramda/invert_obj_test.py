from ramda.invert_obj import invert_obj
from ramda.private.asserts import *


def test_invert_obj():
    race_results = {"first": "alice", "second": "jake"}
    assert_equal(invert_obj(race_results), {"alice": "first", "jake": "second"})


def test_invert_array():
    race2_results = ["alice", "jake"]
    assert_equal(invert_obj(race2_results), {"alice": 0, "jake": 1})
