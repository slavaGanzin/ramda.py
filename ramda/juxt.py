def juxt(fs):
    """juxt applies a list of functions to a list of values"""
    return lambda *args: [f(*args) for f in fs]
