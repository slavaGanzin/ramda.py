from toolz import curry
import re


@curry
def split(separator, string):
    """Splits a string into an array of strings based on the given
    separator"""
    return re.split(separator, string)
