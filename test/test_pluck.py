from ramda import pluck


data = [{"a": "a1", "b": "b1"}, {1: 1, 2: 2}, {"a": "a2", "b": "b2"}]


def test_a():
    assert pluck("a", data) == ["a1", None, "a2"]


def test_one():
    assert pluck(1, data) == [None, 1, None]


def test_iterator():
    assert pluck(None, map(lambda x: x, [{None: 1}])) == [1]
