from toolz import curry


getitem = curry(lambda key, collection: collection[key])
