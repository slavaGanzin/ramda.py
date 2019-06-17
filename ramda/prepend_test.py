from ramda.prepend import prepend
from ramda.private.asserts import *


def prepend_test():
    assert_equal(prepend("fee", ["fi", "fo", "fum"]), ["fee", "fi", "fo", "fum"])
