import pytest

from descriptor.validator import PositiveNumber


@pytest.fixture()
def car():

    class Car:
        speed = PositiveNumber()

    return Car()


class TestPositiveNumberValidator:

    def test_number(self, car):
        with pytest.raises(TypeError):
            car.speed = 'wrrrr'

    def test_positive_number(self, car):
        with pytest.raises(ValueError):
            car.speed = -100500

        car.speed = 120
        assert car.speed == 120
