def nth_arg(n):
    """Returns a function which returns its nth argument"""
    return lambda *args: args[n]
