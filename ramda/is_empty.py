def is_empty(xs):
    try:
        return len(xs) == 0
    except TypeError:
        return False
