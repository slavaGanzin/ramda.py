import inspect
from ramda.private.asserts import assert_equal
from ramda.nAry import nAry


def takes_two_args(a, b):
    return [a, b]


takes_no_arg = nAry(0, takes_two_args)
takes_one_arg = nAry(1, takes_two_args)


@nAry(3)
def takes_three_args(a, b):
    return [a, b]


def n_args(f):
    return len(inspect.signature(f).parameters)


def nAry_curry_test():
    assert_equal(n_args(takes_one_arg), 1)
    assert_equal(n_args(takes_three_args), 3)
    assert_equal(n_args(takes_two_args), 2)

    assert_equal(takes_one_arg(1), [1, None])
    try:
        takes_one_arg(1, 2, 3)
        assert False, 'takes_one_arg(1,2,3) should throw'
    except TypeError:
        pass
    try:
        takes_one_arg()
        assert False, 'takes_one_arg() should throw'
    except TypeError:
        pass

    assert_equal(takes_no_arg(), [None, None])

    try:
        takes_no_arg(1)
        assert False, 'takes_no_arg(1) should throw'
    except TypeError:
        pass

    try:
        nAry(-1)(lambda: 1)
        assert False, 'nAry(-1)(print) should throw'
    except ValueError:
        pass

    assert_equal(nAry(20)(lambda: 1)(*range(0, 20)), 1)
