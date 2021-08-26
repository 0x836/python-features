def make_limiter():
    """
    >>> limit = make_limiter()
    >>> _ = [limit(speed) for speed in (10, 20, 90, 100)]

    Объект limit сохраняет состояние в свободной переменной (free vars) в откомпилированном теле функции:
    >>> limit.__code__.co_varnames
    ('speed', 'over_speeds')
    >>> limit.__code__.co_freevars
    ('speeds',)
    >>> limit.__closure__[0].cell_contents
    [10, 20, 90, 100]
    """

    speeds = []

    def limiter(speed: int):
        """
        Функция-замыкание (функция, которая запоминает привязки свободных переменных, существовавшие на момент
        определения функции, так что их можно использовать впоследствии при вызове функции, когда область видимости,
        в которой она была определена, уже не существует)
        """
        speeds.append(speed)
        over_speeds = sum(speed > 90 for speed in speeds)
        if over_speeds > 3:
            print('айайай')

    return limiter


def make_limiter_improved():
    """
    Чуть более корректная версия, которая хранит не все соостояния, а только результат
    >>> limit = make_limiter_improved()
    >>> _ = [limit(speed) for speed in (30, 50, 120)]
    >>> limit.__code__.co_varnames
    ('speed',)
    >>> limit.__code__.co_freevars
    ('over_speeds',)
    >>> limit.__closure__[0].cell_contents
    1
    """
    over_speeds = 0

    def limiter(speed: int):
        # Свободная переменная over_speeds - неизменяемого типа - при присвоении создается переменная локальной
        # области видимости. А в данном случае вообще будет UnboundLocalError
        nonlocal over_speeds
        if speed > 90:
            over_speeds += 1

        if over_speeds > 3:
            print('айайай')

    return limiter
