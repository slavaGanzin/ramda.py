from .group_by import group_by
from ramda.private.asserts import assert_equal


def grade(student):
    score = student["score"]
    if score < 65:
        return "F"
    if score < 70:
        return "D"
    if score < 80:
        return "C"
    if score < 90:
        return "B"
    return "A"


students = [
    {"name": "Abby", "score": 84},
    {"name": "Donald", "score": 85},
    {"name": "Eddy", "score": 58},
    {"name": "Jack", "score": 69},
]

students_by_grade = {
    "B": [{"name": "Abby", "score": 84}, {"name": "Donald", "score": 85}],
    "F": [{"name": "Eddy", "score": 58}],
    "D": [{"name": "Jack", "score": 69}],
}


def group_by_curry_test():
    assert_equal(group_by(grade)(students), students_by_grade)


def group_by_no_curry_test():
    assert_equal(group_by(grade, students), students_by_grade)


def group_by_empty():
    assert_equal(group_by(grade)([]), {})
