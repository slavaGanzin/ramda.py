from ramda import curry


@curry
def take_while(predicate, list):
    """Returns a new list containing the first n elements of a given list,
    passing each value to the supplied predicate function, and terminating when
    the predicate function returns false. Excludes the element that caused the
    predicate function to fail. The predicate function is passed one argument:
    (value).
    Dispatches to the takeWhile method of the second argument, if present.
    Acts as a transducer if a transformer is given in list position"""
    for i, e in enumerate(list):
        if not predicate(e):
            return list[:i]
    return list
