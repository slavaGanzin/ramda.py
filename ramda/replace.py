from toolz import curry
import re


@curry
def replace(pattern, replacement, string):
    """Replace a substring or regex match in a string with a replacement"""
    return re.sub(pattern, replacement, string)
