from toolz import curry
from ramda.map import map


@curry
def for_each(f, xs):
    """Iterate over an input list, calling a provided function fn for each
    element in the list.
    fn receives one argument: (value).
    Note: R.forEach does not skip deleted or unassigned indices (sparse
    arrays), unlike the native Array.prototype.forEach method. For more
    details on this behavior, see:
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach#Description
    Also note that, unlike Array.prototype.forEach, Ramda's forEach returns
    the original array. In some libraries this function is named each.
    Dispatches to the forEach method of the second argument, if present"""
    map(f, xs)
    return xs
