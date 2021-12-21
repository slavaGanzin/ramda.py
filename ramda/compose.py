from ramda.add import add
from ramda.negate import negate


def compose(*functions):
    """Performs right-to-left function composition. The rightmost function may have
    any arity; the remaining functions must be unary.
    Note: The result of compose is not automatically curried"""

    def composed_functions(*args):
        acc = functions[-1](*args)

        for f in functions[::-1][1::]:
            acc = f(acc)
        return acc

    return composed_functions
