from ramda.function.curry import curry


getitem = curry(lambda key, collection: collection[key])
