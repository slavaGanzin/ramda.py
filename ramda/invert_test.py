from ramda.invert import invert
from ramda.private.asserts import *


race_results_by_first_name = {"first": "alice", "second": "jake", "third": "alice"}


def invert_test():
    assert_equal(
        invert(race_results_by_first_name),
        {"alice": ["first", "third"], "jake": ["second"]},
    )
