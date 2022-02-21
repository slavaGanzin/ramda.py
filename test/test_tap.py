from ramda import tap
from ramda.private.asserts import assert_equal


def test_tap():
    called_box = [False]

    def set_called(v):
        called_box[0] = True

    assert_equal(tap(set_called, 42), 42)
    assert called_box[0]
