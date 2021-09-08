import logging
import time
from functools import partial, wraps
from typing import Callable

logging.basicConfig(level=logging.INFO)


def timer(_func: Callable = None, *, print_logs: bool = True) -> Callable:
    """
    Декоратор с опциональными параметрами.
    Фабрика, которая возвращает функцию (декоратор по сути), которая возвращает функцию, оборачивающую целевую функцию.
    Параметры логично сделать keyword-only

    >>> @timer
    ... def do_something():
    ...     ...
    >>> do_something()

    >>> @timer(print_logs=False)
    ... def do_something():
    ...     ...
    >>> do_something()
    """
    def timer_dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            exec_time = time.perf_counter() - start
            if print_logs:
                logging.info(f'Exec time of {func.__name__}: {exec_time} sec')
            return result
        return wrapper

    if _func is not None:
        return timer_dec(_func)
    else:
        return timer_dec


def another_optional_dec(func: Callable = None, *, some_arg=None, another_arg=None):
    """
    Другой способ сделать то же самое

    >>> @another_optional_dec
    ... def do_something():
    ...     ...
    >>> do_something()

    >>> @another_optional_dec(some_arg=1, another_arg=2)
    ... def do_something():
    ...     ...
    >>> do_something()
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    if func is None:
        return partial(another_optional_dec, some_arg=some_arg, another_arg=another_arg)
    return wrapper


def without_sugar():
    """
    >>> without_sugar = another_optional_dec(without_sugar, some_arg=1)
    >>> without_sugar()

    >>> without_sugar = another_optional_dec(without_sugar)
    >>> without_sugar()
    """
    ...
