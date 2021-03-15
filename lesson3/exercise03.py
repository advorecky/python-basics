# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(var_1, var_2, var_3):
    if var_2 > var_1 < var_3:
        return var_2 + var_3
    elif var_1 > var_2 < var_3:
        return var_1 + var_3
    else:
        return var_1 + var_2


first_digit = float(input("Введите первое число: "))
second_digit = float(input("Введите второе число: "))
third_digit = float(input("Введите третье число: "))

print(my_func(first_digit, second_digit, third_digit))
