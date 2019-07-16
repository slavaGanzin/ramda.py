from toolz import curry
from ramda.juxt import juxt
from ramda.filter import filter
from ramda.reject import reject

partition = juxt([filter, reject])
