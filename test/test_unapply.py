from ramda import *
from ramda.private.asserts import *
import json


def test_unapply():
    assert_equal(unapply(json.dumps)(1, 2, 3), "[1, 2, 3]")
