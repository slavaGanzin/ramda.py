from ramda.private.asserts import *
from ramda.invoker import invoker


def invoker_test():
    replacer = invoker(2, "replace")
    assert_equal(replacer("abcdef", "", "abcdefghijklm"), "ghijklm")
    replace_all = invoker(2, "replace")("abcdefghijklm")
    assert_equal(replace_all("gh", "abcdefghijklm"), "gh")
