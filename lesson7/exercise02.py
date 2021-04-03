# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. "
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def required_fabric(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def _get_required_fabric(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, size):
        self._size = size
        self._required_fabric = 0

        self._clothes.append(self)

    def _get_required_fabric(self):
        pass

    @property
    def required_fabric(self):
        if not self._required_fabric:
            self._get_required_fabric()

        return self._required_fabric

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        self._required_fabric = None

    @property
    def total_required_fabric(self):
        return f"Общий расхода ткани составит {round(sum([item.required_fabric for item in self._clothes]), 1)} попугаев"


class Coat(Clothes):
    def _get_required_fabric(self):
        self._required_fabric = round(self.size / 6.5 + 0.5, 1)

    @property
    def V(self):
        return self.size

    @V.setter
    def V(self, size):
        self.size = size

    def __str__(self):
        return f"Для пальто {self.size} размера расход ткани составит {self.required_fabric} попугаев ткани"


class Costume(Clothes):
    def _get_required_fabric(self):
        self._required_fabric = round(2 * self.size + 0.3, 1)

    @property
    def H(self):
        return self.size

    @H.setter
    def H(self, height):
        self.size = height

    def __str__(self):
        return f"Для роста {self.size} расход ткани для костюма составит {self.required_fabric} попугаев ткани"


clothes = Clothes(0)
coat = Coat(42)
costume = Costume(170)
print(coat)
print(costume)
print(clothes.total_required_fabric)
