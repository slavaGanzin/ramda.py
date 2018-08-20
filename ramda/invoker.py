from ramda.curry import curry


@curry
def invoker(arity, f):
    _args = ', '.join([f"x{i}" for i in range(0, arity)])
    _f = f'lambda {_args}, object: getattr(object, "{f}")({_args})'
    return curry(eval(_f))
