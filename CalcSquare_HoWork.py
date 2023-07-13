# HOMEWORK Square 5.07.2023
# 1)  Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.

class main_square:
    def __init__(self):
        self._result = 0

    def __del__(self):
        self._result = 0
    pass

    @staticmethod
    def side_square(self, a, b, c, d):
        self._result = a and b and c and d
        return self._result

    @staticmethod
    def diagonal(self, a, e):
 #      e = a * √2 or e^2 = 2a^2
        self._result = 2*(a**2) == e
        return self._result

    @staticmethod
    def perimeter_square(self, a, b, c, d):
        self._result = a + b + c + d
        return self._result