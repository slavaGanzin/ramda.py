from toolz import curry
from ramda.clone import clone


@curry
def apply_spec(spec):
    """Given a spec object recursively mapping properties to functions, creates a
    function producing an object of the same structure, by mapping each property
    to the result of calling its associated function with the supplied arguments"""
    out = clone(spec)

    def spec_applier(*args):
        for k, v in spec.items():
            try:
                v.items()
                out[k] = apply_spec(v)(*args)
            except AttributeError:
                out[k] = v(*args)
        return out

    return spec_applier
