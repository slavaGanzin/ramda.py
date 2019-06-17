from ramda import *
from ramda.private.asserts import *

alice = {"name": "ALICE", "age": 101}
favorite = prop("favoriteLibrary")
favorite_with_default = prop_or("Ramda", "favoriteLibrary")


def prop_or_test():
    assert_equal(favorite(alice), None)
    assert_equal(favorite_with_default(alice), "Ramda")
