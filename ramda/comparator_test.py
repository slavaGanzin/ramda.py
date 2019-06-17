from ramda import *
from ramda.private.asserts import *


def comparator_test():
    by_age = comparator(lambda a, b: a["age"] < b["age"])
    people = [{"name": "a", "age": 22}, {"name": "b", "age": 14}]
    people_by_increasing_age = sort(by_age, people)

    assert_equal(people_by_increasing_age, list(reversed(people)))
