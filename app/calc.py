import pytest
from app.calc import Calculator  # Импортируем класс Calculator

class TestCalc:
    def setup_method(self):  # Используем setup_method для подготовки перед каждым тестом
        self.calc = Calculator()  # Создаём экземпляр Calculator

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2  # Проверяем метод adding

    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) != 3  # Проверяем, что результат не 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):  # Проверка на ZeroDivisionError
            self.calc.division(1, 0)
