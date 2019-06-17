from ramda import *
from ramda.private.asserts import *


alice = {"name": "alice", "age": 40}
bob = {"name": "bob", "age": 30}
clara = {"name": "clara", "age": 40}

people = [clara, bob, alice]

age_name_sort = sort_with([descend(prop("age")), ascend(prop("name"))])


def sort_with_test():
    assert_equal(age_name_sort(people), [alice, clara, bob])
