# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_right(self):
        return f"{self.name} повернула направо"

    def turn_left(self):
        return f"{self.name} повернула налево"

    def show_speed(self):
        return f"{self.speed} км/ч"


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)

    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            return f"{self.speed}. {self.name} превысила скорость на {self.speed - max_speed} км/ч"
        else:
            return f"{self.speed} км/ч"


class SportCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)

    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            return f"{self.speed} км/ч. {self.name} превысила скорость на {self.speed - max_speed} км/ч"
        else:
            return f"{self.speed} км/ч"


class PoliceCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed)
        self.is_police = True
