import hashlib
import json
from ramda.memoize_with import memoize_with


def memoize(f):
    def hash(*args):
        return hashlib.sha256(
            json.dumps(args).encode("utf-8")
        ).hexdigest()

    return memoize_with(hash, f)
