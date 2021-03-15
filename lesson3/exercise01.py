# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(var_1, var_2):
    if var_2 == 0:
        return "Нельзя делить на ноль"
    else:
        return var_1 / var_2


try:
    first_digit = float(input("Укажите первое число: "))
    second_digit = float(input("Укажите второе число: "))
    print(division(first_digit, second_digit))
except ValueError:
    print("Введены нечисловые данные")
