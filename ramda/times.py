from toolz import curry


@curry
def times(function, n):
    """Calls an input function n times, returning an array containing the results of those function calls. fn is passed one argument: The current value of n, which begins at 0 and is gradually incremented to n - 1."""
    return [function(i) for i in range(0, n)]
