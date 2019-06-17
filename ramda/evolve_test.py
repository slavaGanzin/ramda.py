from ramda.private.asserts import *
from ramda.evolve import evolve
from ramda.trim import trim
from ramda.add import add

tomato = {
    "firstName": "  Tomato ",
    "data": {"elapsed": 100, "remaining": 1400},
    "id": 123,
}

transformations = {
    "firstName": trim,
    "lastName": trim,  # Will not get invoked.
    "data": {"elapsed": add(1), "remaining": add(-1)},
}


def evolve_test():
    assert_equal(
        evolve(transformations, tomato),
        {"firstName": "Tomato", "data": {"elapsed": 101, "remaining": 1399}, "id": 123},
    )
