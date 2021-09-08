from abc import ABC, abstractmethod


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class PositiveNumber(Validator):

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'{value} must be int or float')
        if value < 0:
            raise ValueError(f'{value} must be > 0')
