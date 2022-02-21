# -*- coding: utf-8 -*-
from ramda import trim
from ramda.private.asserts import assert_equal


def test_trim():
    assert_equal(trim("      xx "), "xx")


def test_trim_utf():
    assert_equal(trim("      її  "), "її")
