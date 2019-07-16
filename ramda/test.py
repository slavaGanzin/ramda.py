from toolz import curry
import re


@curry
def test(pattern, string):
    """Determines whether a given string matches a given regular expression"""
    return bool(re.search(pattern, string))
