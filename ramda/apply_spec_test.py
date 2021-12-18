from ramda import *
from ramda.private.asserts import *


get_metrics = apply_spec({"sum": add, "nested": {"mul": multiply}})


def apply_spec_test():
    assert_equal(get_metrics(2, 4), {"sum": 6, "nested": {"mul": 8}})

    res = map(
        apply_spec(
            {
                "foo": prop("bar"),
            }
        ),
        [{"bar": 1}, {"bar": 2}],
    )
    assert res == [{"foo": 1}, {"foo": 2}]
