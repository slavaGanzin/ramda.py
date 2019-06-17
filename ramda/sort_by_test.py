from ramda import *
from ramda.private.asserts import *


sort_by_first_item = sort_by(prop(0))
sort_by_name_case_insensitive = sort_by(compose(to_lower, prop("name")))
pairs = [[-1, 1], [-2, 2], [-3, 3]]

alice = {"name": "ALICE", "age": 101}
bob = {"name": "Bob", "age": -10}
clara = {"name": "clara", "age": 314.159}

people = [clara, bob, alice]


def sort_by_test():
    assert_equal(sort_by_first_item(pairs), [[-3, 3], [-2, 2], [-1, 1]])

    assert_equal(sort_by_name_case_insensitive(people), [alice, bob, clara])
