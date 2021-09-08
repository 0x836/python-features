import functools
from typing import Callable

ARG1 = 'arg1'
ARG2 = 'arg2'


def simple_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@simple_decorator
def do_something(*args, **kwargs):
    """
    >>> do_something(ARG1, arg2=ARG2)
    """
    ...


def without_sugar(arg1, arg2):
    """
    >>> without_sugar = simple_decorator(without_sugar)
    >>> without_sugar(ARG1, ARG2)
    """
    ...
