from ramda.private.asserts import *
from ramda.invoker import invoker


def test_invoker():
    replacer = invoker(2, "replace")
    assert_equal(replacer("abcdef", "", "abcdefghijklm"), "ghijklm")
    replace_all = invoker(2, "replace")("abcdefghijklm")
    assert_equal(replace_all("gh", "abcdefghijklm"), "gh")

    class TestClass:
        def one(self):
            return 1

    one = invoker(0, "one")(TestClass())
    assert one == 1
