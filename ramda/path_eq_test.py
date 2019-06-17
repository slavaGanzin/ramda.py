from ramda.path_eq import path_eq
from ramda.filter import filter
from ramda.private.asserts import *

user1 = {"address": {"zipCode": 90210}}
user2 = {"address": {"zipCode": 55555}}
user3 = {"name": "Bob"}
users = [user1, user2, user3]


def path_eq_test():
    is_famous = path_eq(["address", "zipCode"], 90210)
    assert_equal(filter(is_famous, users), [user1])
