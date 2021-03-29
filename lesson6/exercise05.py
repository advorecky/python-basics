# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from exercise04 import TownCar, SportCar, WorkCar, PoliceCar

town_car = TownCar("Ford Focus", "Blue", 58)
sport_car = SportCar("Ferrari F40", "Red", 284)
work_car = WorkCar("Chevrolet Silverado", "White", 45)
police_car = PoliceCar("Dodge Charger", "Black & White", 92)


print(f"{town_car.color} {town_car.go()} со скоростью {town_car.show_speed()}")
print(f"{sport_car.color} {sport_car.go()} со скоростью {sport_car.show_speed()}")
print(f"{police_car.name} не остановила {sport_car.name}, т.к. не смогла разогнаться выше {police_car.show_speed()}")
print(f"{police_car.name} остановила {work_car.name}, двигавшуюся со скоростью {work_car.show_speed()}")
