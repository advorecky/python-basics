# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()). Данные методы должны
# применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток. В классе необходимо
# реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
#
# Подсказка: подробный список операторов для перегрузки доступен по ссылке https://pythonworld.ru/osnovy/peregruzka-operatorov.html.

class Cell:
    def __init__(self, number_of_cells: int):
        self._number_of_cells = number_of_cells

    def __str__(self):
        return f"Ячеек в клетке: {self._number_of_cells}"

    def __add__(self, other):
        return Cell(self._number_of_cells + other._number_of_cells)

    def __sub__(self, other):
        if self._number_of_cells < other._number_of_cells:
            return "Разность количества ячеек двух клеток меньше нуля"
        else:
            return Cell(self._number_of_cells - other._number_of_cells)

    def __mul__(self, other):
        return Cell(self._number_of_cells * other._number_of_cells)

    def __truediv__(self, other):
        return Cell(self._number_of_cells // other._number_of_cells)

    def make_order(self, cells_in_sequence):
        sequence = ""
        for __cell in range(int(self._number_of_cells / cells_in_sequence)):
            sequence += f"{'*' * cells_in_sequence} \n"
        sequence += f"{'*' * (self._number_of_cells % cells_in_sequence)} \n"
        return sequence


cell_example_01 = Cell(11)
cell_example_02 = Cell(2)
print(cell_example_01)
print(cell_example_02)
print(cell_example_01 + cell_example_02)
print(cell_example_01 - cell_example_02)
print(cell_example_02 - cell_example_01)
print(cell_example_01 / cell_example_02)
print(cell_example_01.make_order(10))
print(cell_example_02.make_order(5))
