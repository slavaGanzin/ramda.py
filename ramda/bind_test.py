from ramda.private.asserts import assert_equal
from ramda.bind import bind


def f(self):
    return self.name()


class C(object):
    def name(self):
        return "C"


def no_bind_test():
    assert_equal(f(C()), "C")


def bind_nocurry_test():
    assert_equal(bind(f)(C())(), "C")


def bind_curry_test():
    assert_equal(bind(f, C())(), "C")
