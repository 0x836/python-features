import time
import logging
from typing import Callable

logger = logging.getLogger(__name__)


def timer(func: Callable):
    def wrapper():
        start = time.perf_counter()
        result = func()
        exec_time = time.perf_counter() - start
        logger.info(f'Exec time of {func.__name__}: {exec_time}')
        return result
    return wrapper


def without_sugar():
    """
    >>> without_sugar = timer(without_sugar)
    >>> without_sugar()
    """
    ...


@timer
def with_sugar():
    """
    >>> with_sugar()
    """
    ...
