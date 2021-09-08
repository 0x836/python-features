from time import sleep


class LazyProperty:
    """
    Вся суть в том, что это должен быть non-data descriptor.
    При первом обращении к аттрибуту выполнится __get__, а в нём мы положили результат выполнения декорированной
    функции в __dict__ инстанса с таким же названием, как аттрибут (функция в данном случае).
    Таким образом, при последующих обращениях к аттрибуту, он будет браться из дикта инстанса, а не из дескриптора,
    поскольку в attribute lookup'е приоритет аттрибута инстанса выше, чем non-data descriptor.
    Соответственно, важно не забывать, что дескриптор должен быть non-data - не иметь __set__ или __delete__,
    тогда LazyProperty превратится в просто Property
    """

    def __init__(self, func):
        # Будем использовать как декоратор, значит передается декорируемая функция
        self._func = func
        self._func_name = func.__name__

    def __get__(self, instance, owner):
        result = self._func(instance)
        instance.__dict__[self._func_name] = result
        return result


class Foo:

    @LazyProperty
    def bar(self):
        print('counting')
        sleep(5)
        return 'bar'


if __name__ == '__main__':
    foo = Foo()
    print(foo.bar)
    print(foo.bar)
