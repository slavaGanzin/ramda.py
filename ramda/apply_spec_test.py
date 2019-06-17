from ramda import *
from ramda.private.asserts import *


get_metrics = apply_spec({"sum": add, "nested": {"mul": multiply}})


def apply_spec_test():
    assert_equal(get_metrics(2, 4), {"sum": 6, "nested": {"mul": 8}})
