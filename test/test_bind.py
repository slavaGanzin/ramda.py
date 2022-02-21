from ramda.private.asserts import assert_equal
from ramda.bind import bind


def f(self):
    return self.name()


class C(object):
    def name(self):
        return "C"


def test_no_bind():
    assert_equal(f(C()), "C")


def test_bind_nocurry():
    assert_equal(bind(f)(C())(), "C")


def test_bind_curry():
    assert_equal(bind(f, C())(), "C")
