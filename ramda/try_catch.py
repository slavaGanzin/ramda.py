from toolz import curry
import inspect


@curry
def try_catch(tryer, catcher):
    """tryCatch takes two functions, a tryer and a catcher. The returned
    function evaluates the tryer; if it does not throw, it simply returns the
    result. If the tryer does throw, the returned function evaluates the
    catcher function and returns its result. Note that for effective
    composition with this function, both the tryer and catcher functions
    must return the same type of results"""

    if inspect.iscoroutinefunction(tryer):

        async def async_exe(*args):
            try:
                return await tryer(*args)
            except Exception as e:
                return catcher(e, *args)

        return async_exe

    else:

        def exe(*args):
            try:
                return tryer(*args)
            except Exception as e:
                return catcher(e, *args)

        return exe
