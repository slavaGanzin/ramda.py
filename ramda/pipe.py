from functools import reduce


def pipe(*functions):
    """Performs left-to-right function composition. The leftmost function may have
    any arity; the remaining functions must be unary.
    In some libraries this function is named sequence.
    Note: The result of pipe is not automatically curried"""

    def piped_functions(*args):
        acc = functions[0](*args)

        for f in functions[1::]:
            acc = f(acc)
        return acc

    return piped_functions
