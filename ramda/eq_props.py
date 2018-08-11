from ramda.curry import curry


@curry
def eq_props(prop, object1, object2):
    return object1[prop] == object2[prop]
