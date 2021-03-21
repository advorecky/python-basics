# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

productivity_in_hours, rate_per_hour, bonus = argv[1:]


def payroll(f_productivity_in_hours, f_rate_per_hour, f_bonus):
    return (f_productivity_in_hours * f_rate_per_hour) + f_bonus


try:
    print("Заработная плата сотрудника состаяляет: {} попугаев.".format(
        payroll(float(productivity_in_hours), float(rate_per_hour),
                float(bonus))))
except ValueError:
    print("Введены нечисловые данные")
