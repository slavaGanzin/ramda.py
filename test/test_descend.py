from ramda import *
from ramda.private.asserts import *


alice = {"name": "alice", "age": 40}
bob = {"name": "bob", "age": 30}
clara = {"name": "clara", "age": 40}
people = [clara, bob, alice]


def test_ascend():
    assert_equal(sort(descend(prop("age")), people), [clara, alice, bob])
