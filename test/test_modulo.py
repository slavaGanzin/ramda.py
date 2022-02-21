from ramda import modulo
from ramda.private.asserts import assert_equal


def test_modulo_nocurry():
    assert_equal(modulo(12, 5), 2)
    assert_equal(modulo(-12, 5), 3)


def test_modulo_curry():
    assert_equal(modulo(12)(5), 2)
