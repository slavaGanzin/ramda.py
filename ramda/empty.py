def empty(x):
    """Returns the empty value of its argument's type. Ramda defines the empty
    value of Array ([]), Object ({}), String (''), and Arguments. Other
    types are supported if they define <Type>.empty,
    <Type>.prototype.empty or implement the
    FantasyLand Monoid spec.
    Dispatches to the empty method of the first argument, if present"""
    if x:
        return False
    else:
        return True
