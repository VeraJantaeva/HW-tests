# основы языка программирвоания Python
# Функции - использование встроенных и создание собственных
#  Задание «Квадратное уравнение»
# Все мы в школе решали квадратное уравнение: ax ** 2 + bx + c = 0.
#
# Необходимо автоматизировать этот процесс и написать функцию для нахождения корней уравнения.
# Также реализуйте вспомогательную функцию для нахождения дискриминанта, основываясь на его свойствах:
#
# Если дискриминант < 0, то вывести «корней нет».
# Если дискриминант = 0, то вывести один корень.
# Если дискриминант > 0, то вывести два различных корня.
# Необходимо вывести решение для следующих коэффициентов:
#
# a = 1, b = 8, c = 15.
# a = 1, b = -13, c = 12.
# a = -4, b = 28, c = -49.
# a = 1, b = 1, c = 1.
# На примере можно вспомнить, как работает дискриминант.
# Дискриминант позволяет определить, сколько в уравнении корней.
#
# Решим уравнение: 3x ** 2 - 4 * x + 2 = 0.
# Сначала определим коэффициенты: a = 3, b = -4, c = 2.
# Рассчитаем дискриминант: D = b ** 2 - 4 * a * c = (-4) ** 2 - 4 * 3 * 2 = -8.
# Так как дискриминант < 0, значит у уравнения корней нет.
# В результате корректного выполнения задания будет выведен следующий результат:
#
# 1
# 2
# 3
# 4
# -3.0 -5.0
# 12.0 1.0
# 3.5
# корней нет

def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    D = b ** 2 - 4 * a * c
    return D


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    dis = discriminant(a, b, c)
    if dis < 0:
        return None  # корней нет
    elif dis == 0:
        x = - (b / (2 * a))
        return x
    else:
        x_1 = (-b + dis ** 0.5) / (2 * a)
        x_2 = (-b - dis ** 0.5) / (2 * a)
        return (x_1, x_2)

import unittest

class TestQuadraticEquation(unittest.TestCase):
    # Тесты для функции discriminant
    def test_discriminant_positive(self):
        self.assertEqual(discriminant(1, 8, 15), 4)  # D = 8^2 - 4*1*15 = 64 - 60 = 4

    def test_discriminant_zero(self):
        self.assertEqual(discriminant(1, -6, 9), 0)   # D = (-6)^2 - 4*1*9 = 36 - 36 = 0

    def test_discriminant_negative(self):
        self.assertEqual(discriminant(1, 1, 1), -3)   # D = 1^2 - 4*1*1 = 1 - 4 = -3

    # Тесты для функции solution с параметризацией
    def test_solution_no_roots(self):
        self.assertIsNone(solution(1, 1, 1))  # Нет корней

    def test_solution_one_root(self):
        self.assertEqual(solution(1, -6, 9), 3.0)  # Один корень: x = 3

    def test_solution_two_roots(self):
        roots = solution(1, 8, 15)
        self.assertEqual(len(roots), 2)  # Два корня
        self.assertAlmostEqual(roots[0], -3.0)  # x1 ≈ -3.0
        self.assertAlmostEqual(roots[1], -5.0)  # x2 ≈ -5.0


if __name__ == '__main__':
    unittest.main()