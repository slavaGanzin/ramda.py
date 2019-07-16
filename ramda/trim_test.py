# -*- coding: utf-8 -*-
from .trim import trim
from ramda.private.asserts import assert_equal


def trim_test():
    assert_equal(trim("      xx "), "xx")


def trim_utf_test():
    assert_equal(trim("      її  "), "її")
