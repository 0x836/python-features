import functools
from typing import Callable


def some_dec_unwrap(func: Callable) -> Callable:
    def wrapper():
        """Wrapper"""
        return func()
    return wrapper


@some_dec_unwrap
def do_something():
    ...


def some_dec_wrap(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
        """Another wrapper"""
        return func()
    return wrapper


@some_dec_wrap
def do_something_else():
    """Do something else"""
    ...
