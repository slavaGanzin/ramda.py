from ramda.obj_of import obj_of
from ramda.compose import compose
from ramda.map import map
from ramda.private.asserts import *


match_phrases = compose(obj_of("must"), map(obj_of("match_phrase")))


def obj_of_test():
    assert_equal(
        match_phrases(["foo", "bar", "baz"]),
        {
            "must": [
                {"match_phrase": "foo"},
                {"match_phrase": "bar"},
                {"match_phrase": "baz"},
            ]
        },
    )
