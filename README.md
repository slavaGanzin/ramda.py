# ramda.py [![Build Status](https://travis-ci.org/slavaGanzin/ramda.py.svg?branch=master)](https://travis-ci.org/slavaGanzin/ramda.py) [![Coverage Status](https://coveralls.io/repos/github/slavaGanzin/ramda.py/badge.svg?branch=master)](https://coveralls.io/github/slavaGanzin/ramda.py?branch=master)

Python Clone of [Ramda.js](http://ramdajs.com)

```sh
pip install ramda
```

```python
>>> from ramda import *
>>> inc(1)
2
>>> map(inc, [1, 2, 3])
[2, 3, 4]
>>> incEach = map(inc)
>>> incEach([1, 2, 3])
[2, 3, 4]
```

Improved fork of [Jack Firth's original impementation](https://github.com/jackfirth/pyramda)
