# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list[list]):
        self._matrix = matrix
        _matrix_rows = len(self._matrix)
        self._matrix_size = set([(_matrix_rows, len(row))
                                for row in self._matrix])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self._matrix])

    def __add__(self, other):
        result = []
        for i in zip(self._matrix, other._matrix):
            result.append([sum([j, k]) for j, k in zip(*i)])
        return Matrix(result)


matrix_example_01 = Matrix([[31, 22], [37, 43], [51, 86]])
print(matrix_example_01, "\n")

matrix_example_02 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix_example_02, "\n")

matrix_example_03 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix_example_03, "\n")

print(matrix_example_01 + matrix_example_02 + matrix_example_03)
