from toolz import curry


@curry
def invoker(arity, f):
    """Turns a named method with a specified arity into a function that can be
    called directly supplied with arguments and a target object.
    The returned function is curried and accepts arity + 1 parameters where
    the final parameter is the target object"""
    _args = "".join([f"x{i}, " for i in range(0, arity)])
    _f = f'lambda {_args} object: getattr(object, "{f}")({_args})'
    return curry(eval(_f))
