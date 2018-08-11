from ramda.curry import curry


@curry
def ends_with(needle, haystack):
    return haystack[-len(needle):] == needle
