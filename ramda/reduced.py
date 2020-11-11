import collections


class Reduced:
    def __init__(self, value):
        self.value = value

    def unwrap(self):
        return self.value


def reduced(value):
    """Returns a value wrapped to indicate that it is the final value of the reduce
    and transduce functions. The returned value should be considered a black
    box: the internal structure is not guaranteed to be stable.
    Note: this optimization is unavailable to functions not explicitly listed
    above. For instance, it is not currently supported by
    reduceRight"""
    return Reduced(value)
