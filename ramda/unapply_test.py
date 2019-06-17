from ramda import *
from ramda.private.asserts import *
import json


def unapply_test():
    assert_equal(unapply(json.dumps)(1, 2, 3), "[1, 2, 3]")
