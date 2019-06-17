from ramda.project import project
from ramda.private.asserts import *


abby = {"name": "Abby", "age": 7, "hair": "blond", "grade": 2}
fred = {"name": "Fred", "age": 12, "hair": "brown", "grade": 7}
kids = [abby, fred]


def project_test():
    assert_equal(
        project(["name", "grade"], kids),
        [{"name": "Abby", "grade": 2}, {"name": "Fred", "grade": 7}],
    )
