import pytest

# Функция для проверки, можно ли составить треугольник
def is_triangle(a, b, c):
    """Проверяет, можно ли составить треугольник из трёх отрезков."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


# Тесты для функции
@pytest.mark.parametrize("a, b, c", [
    # Негативные тесты
    (-1, 2, 3),   # Отрицательная длина
    (2, -1, 3),
    (2, 3, -1),
    (0, 3, 4),    # Нулевая длина
    (3, 0, 4),
    (3, 4, 0),
    (1, 2, 10),   # Длины, из которых невозможно составить треугольник
    (10, 2, 1),
    (1, 10, 2),
])
def test_is_not_triangle(a, b, c):
    """Негативные тесты: проверить, что из этих длин нельзя составить треугольник."""
    assert not is_triangle(a, b, c)


@pytest.mark.parametrize("a, b, c", [
    # Позитивные тесты
    (3, 4, 5),     # Пифагоров треугольник
    (6, 8, 10),    # Ещё один Пифагоров треугольник
    (7, 7, 7),     # Равносторонний треугольник
    (5, 7, 10),    # Разносторонний треугольник
])
def test_is_triangle(a, b, c):
    """Позитивные тесты: проверить, что из этих длин можно составить треугольник."""
    assert is_triangle(a, b, c)