from .replace import replace
from ramda.private.asserts import assert_equal


def replace_nocurry_test():
    assert_equal(replace('a', 'b', 'aa'), 'bb')


def replace_curry_test():
    assert_equal(replace('a', 'b')('aa'), 'bb')


def replace_curry_regex_test():
    assert_equal(replace(r'a+', 'b')('aa'), 'b')
