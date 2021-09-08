from functools import partial, wraps
from typing import Callable


def dec1(func: Callable = None, *, arg=None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    if func is None:
        return partial(dec1, arg=arg)
    return wrapper


def dec2(_func: Callable = None, *, arg=None):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arg:
                ...
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper
    if _func is not None:
        return deco(_func)
    return deco


@dec1(arg=1)
@dec2
def do_something():
    """
    Порядок применения декораторов - прямой
    >>> do_something()
    Decorator 1
    Decorator 2
    """
    ...
