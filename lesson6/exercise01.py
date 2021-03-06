# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color: str
    __modes = {'red': 7,
               'yellow': 2,
               'green': 30}

    def running(self):
        for color, wait_seconds in self.__modes.items():
            self.__color = color
            print(f"Await {self.__color} color for {wait_seconds} seconds")
            sleep(wait_seconds)


traffic_light = TrafficLight()
traffic_light.running()
