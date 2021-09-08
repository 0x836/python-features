import time
import types
from functools import wraps
from typing import Callable


class Timer:
    """timer"""

    def __init__(self, func: Callable):
        wraps(func)(self)
        self._func = func

    def __call__(self, *args, **kwargs):
        """call"""
        start = time.perf_counter()
        result = self._func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        print(f'Exec time of {self._func.__name__}: {exec_time}')
        return result

    def __get__(self, instance, cls):
        """
        Для использования декоратора для методов классов необходимо воссоздать протокол non-data деструкторов - точно
        так же, как это делают обычные методы в классе.
        """
        if instance is None:
            # в случае, если метод вызывается у класса.
            # >>> Class.Foo() (foo декорирован)
            # а фактически это не метод - это объект-функция класса.
            # её и вернём
            return self
        else:
            # в случае, когда метод вызывается у инстанса.
            # это уже bound-method, собственно, вручную и сбаундим функцию (а точнее, весь объект-декоратор) в метод
            return types.MethodType(self, instance)


@Timer
def foo(*args, **kwargs):
    """foo"""
    pass


class Foo:
    @Timer
    def bar(self):
        pass


if __name__ == '__main__':
    foo()

    Foo().bar()
