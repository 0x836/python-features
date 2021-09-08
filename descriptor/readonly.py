class ReadOnlyDescriptor:
    """
    Для реализации readonly аттрибута с помощью дескриптора необходимо сделать из него data-дескриптор.
    Потому что в случае, если в дескрипторе реализован только __get__, то он является non-data дескриптором,
    и приоритет в attribute lookup'е у него ниже, чем у аттрибута инстанса.
    То есть в случае присвоения мы не получим readonly эффект, мы просто создадим новый перекрывающий аттрибут
    в инстансе (примеры в доктесте выглядят не очень, см. в test/test_readonly.py).
    Поэтому рекомендуется реализовать метод __set__ с вызовом AttributeError
    """

    def __get__(self, instance, owner):
        return 'hello'

    def __set__(self, instance, value):
        raise AttributeError('Cannot change the value')


class NotReadOnlyDescriptor:
    def __get__(self, instance, owner):
        return 'hello'


class HelloMan:
    greeting_speech = ReadOnlyDescriptor()
    changing_greetings = NotReadOnlyDescriptor()
