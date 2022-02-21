from ramda.prepend import prepend
from ramda.private.asserts import *


def test_prepend():
    assert_equal(prepend("fee", ["fi", "fo", "fum"]), ["fee", "fi", "fo", "fum"])
