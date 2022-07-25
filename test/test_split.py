from ramda import *
from ramda.private.asserts import *

path_components = split("\/")


def test_split():
    assert_equal(
        tail(path_components("/usr/local/bin/node")), ["usr", "local", "bin", "node"]
    )

    assert_equal(split("\.", "a.b.c.xyz.d"), ["a", "b", "c", "xyz", "d"])

    assert_equal(split("\s+", "a b c    xyz  d"), ["a", "b", "c", "xyz", "d"])
