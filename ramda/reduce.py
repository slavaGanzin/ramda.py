from ramda.curry import curry
from functools import reduce as uncurried_reduce


@curry
def reduce(operator, init, vs):
    """Returns a single item by iterating through the list, successively calling
the iterator function and passing it an accumulator value and the current
value from the array, and then passing the result to the next call.
The iterator function receives two values: (acc, value). It may use
R.reduced to shortcut the iteration.
The arguments' order of reduceRight's iterator function
is (value, acc).
Note: R.reduce does not skip deleted or unassigned indices (sparse
arrays), unlike the native Array.prototype.reduce method. For more details
on this behavior, see:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#Description
Dispatches to the reduce method of the third argument, if present. When
doing so, it is up to the user to handle the R.reduced
shortcuting, as this is not implemented by reduce"""
    return uncurried_reduce(operator, vs, init)
