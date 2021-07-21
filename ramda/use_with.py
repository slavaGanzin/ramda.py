from toolz import curry
import inspect


@curry
def use_with(function, transformers):
    """Accepts a function fn and a list of transformer functions and returns a
    new curried function. When the new function is invoked, it calls the
    function fn with parameters consisting of the result of calling each
    supplied handler on successive arguments to the new function.
    If more arguments are passed to the returned function than transformer
    functions, those arguments are passed directly to fn as additional
    parameters. If you expect additional arguments that don't need to be
    transformed, although you can ignore them, it's best to pass an identity
    function so that the new function reports the correct arity"""
    try:
        args = inspect.getfullargspec(function).args
    except TypeError:
        args = ["argument" + str(i) for i, x in enumerate(transformers)]

    F = {function.__name__: function}

    run = []
    for i, t in enumerate(transformers):

        transformer_name = f"fn_{i}" if t.__name__ == "<lambda>" else t.__name__

        F[transformer_name] = t
        try:
            args[i]
        except (IndexError, TypeError):
            args.append("argument" + str(i))

        run.append(transformer_name + "(" + args[i] + ")")
    f = (
        "lambda "
        + ", ".join(args[: len(transformers)])
        + ": "
        + function.__name__
        + "("
        + ",".join(run)
        + ")"
    )
    return curry(eval(f, F))
