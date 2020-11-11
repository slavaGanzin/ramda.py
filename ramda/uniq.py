def uniq(xs):
    """Returns a new list containing only one copy of each element in the original
    list. R.equals is used to determine equality"""
    try:
        return list(set(xs))
    except TypeError:
        u = []

        for x in xs:
            if x not in u:
                u.append(x)
        return u
