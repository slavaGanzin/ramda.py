from ramda import *
from ramda.private.asserts import *


abby = {"name": "Abby", "age": 7, "hair": "blond"}
fred = {"name": "Fred", "age": 12, "hair": "brown"}
rusty = {"name": "Rusty", "age": 10, "hair": "brown"}
alois = {"name": "Alois", "age": 15, "disposition": "surly"}
kids = [abby, fred, rusty, alois]
has_brown_hair = prop_eq("hair", "brown")


def prop_eq_test():
    assert_equal(filter(has_brown_hair, kids), [fred, rusty])
