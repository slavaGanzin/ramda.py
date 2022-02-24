from ramda import *
from ramda.private.asserts import *
import asyncio


def await_(res):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(res)


def test_try_catch():
    assert_equal(try_catch(lambda x: x["x"], F)({"x": True}), True)
    assert_equal(try_catch(lambda x: x["x"], F)(None), False)
    try_catch(lambda: raise_(Exception("foo")), always("caught"))("bar")

    async def asyncx(x):
        return x[0]

    assert_equal(await_(try_catch(asyncx, lambda e, a: e)([[1, 2, 3]])), [1, 2, 3])
    assert_equal(
        isinstance(await_(try_catch(asyncx, lambda e, a: e)([])), IndexError), True
    )
