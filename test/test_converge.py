from ramda.concat import concat
from ramda.converge import converge
from ramda.divide import divide
from ramda.length import length
from ramda.private.asserts import *
from ramda.sum import sum
from ramda.to_lower import to_lower
from ramda.to_upper import to_upper


average = converge(divide, [sum, length])
strangeConcat = converge(concat, [to_upper, to_lower])


def test_average():
    assert_equal(average([1, 2, 3, 4, 5, 6, 7]), 4.0)


def test_concat():
    assert_equal(strangeConcat("Yodel"), "YODELyodel")
