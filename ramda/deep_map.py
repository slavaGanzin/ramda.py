from collections.abc import Mapping
from ramda import curry


@curry
def deep_map(fn, obj):
    def deepget(obj, key=None, drop_keys=0):
        if not key or not obj:
            return obj
        if drop_keys != 0:
            key = key[:-drop_keys]
        for k in key:
            if isinstance(obj, Mapping):
                k = list(obj)[k]  # get key by index (OrderedDict, Python >=3.6)
            obj = obj[k]
        return obj

    def dkey(x, k):
        return list(x)[k] if isinstance(x, Mapping) else k

    def nonempty_iter(item):
        # do not enter empty iterable, since nothing to 'iterate' or apply fn to
        try:
            list(iter(item))
        except:
            return False
        return not isinstance(item, str) and len(item) > 0

    def _process_key(obj, key, depth, revert_tuple_keys, recursive=False):
        container = deepget(obj, key, 1)
        item = deepget(obj, key, 0)

        if nonempty_iter(item) and not recursive:
            depth += 1
        if len(key) == depth:
            if key[-1] == len(container) - 1:  # iterable end reached
                depth -= 1  # exit iterable
                key = key[:-1]  # drop iterable key
                if key in revert_tuple_keys:
                    supercontainer = deepget(obj, key, 1)
                    k = dkey(supercontainer, key[-1])
                    supercontainer[k] = tuple(deepget(obj, key))
                    revert_tuple_keys.pop(revert_tuple_keys.index(key))
                if depth == 0 or len(key) == 0:
                    key = None  # exit flag
                else:
                    # recursively exit iterables, decrementing depth
                    # and dropping last key with each recursion
                    key, depth = _process_key(
                        obj, key, depth, revert_tuple_keys, recursive=True
                    )
            else:  # iterate next element
                key[-1] += 1
        elif depth > len(key):
            key.append(0)  # iterable entry
        return key, depth

    key = [0]
    depth = 1
    revert_tuple_keys = []

    if not nonempty_iter(obj):  # nothing to do here
        raise ValueError(f"input must be a non-empty iterable - got: {obj}")
    elif isinstance(obj, tuple):
        obj = list(obj)
        revert_tuple_keys.append(None)  # revert to tuple at function exit

    while key is not None:
        container = deepget(obj, key, 1)
        item = deepget(obj, key, 0)

        if isinstance(container, tuple):
            ls = list(container)  # cast to list to enable mutating
            ls[key[-1]] = fn(item)

            supercontainer = deepget(obj, key, 2)
            k = dkey(supercontainer, key[-2])
            supercontainer[k] = ls
            revert_tuple_keys.append(key[:-1])  # revert to tuple at iterable exit
        else:
            k = dkey(container, key[-1])
            container[k] = fn(item)

        key, depth = _process_key(obj, key, depth, revert_tuple_keys)

    if None in revert_tuple_keys:
        obj = tuple(obj)
    return obj
