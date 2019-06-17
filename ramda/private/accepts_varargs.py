from inspect import getfullargspec


def argspec_has_varargs(argspec):
    return argspec.varargs is not None or argspec.varkw is not None


def accepts_varargs(f):
    return argspec_has_varargs(getfullargspec(f))
