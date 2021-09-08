class DescriptorProtocol:

    """
    Дескрипторы - объекты, которые:
    - реализуют дескрипторный протокол, содержащий методы __get__, __set__, __delete__ (и/или),
    - являются аттрибутами других объектов
    и позволяющие тем самым задавать поведение этих аттрибутов.
    """

    def __get__(self, instance, owner=None):
        ...

    def __set__(self, instance, value):
        ...

    def __delete__(self, instance):
        ...

    def __set_name__(self, owner, name):
        ...
