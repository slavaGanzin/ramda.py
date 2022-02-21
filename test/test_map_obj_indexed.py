from ramda import map_obj_indexed
from ramda import values
from ramda import inc
from ramda.private.asserts import assert_dicts_equal


test_dict = {"a": 1, "b": 2, "c": 3}

expected_dict = {"a": 2, "b": 3, "c": 4}


def test_map_dict():
    assert_dicts_equal(
        map_obj_indexed(lambda value, key, object: inc(value), test_dict), expected_dict
    )
