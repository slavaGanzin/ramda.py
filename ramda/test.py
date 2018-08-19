from ramda.curry import curry
import re


@curry
def test(pattern, string):
    return bool(re.search(pattern, string))
