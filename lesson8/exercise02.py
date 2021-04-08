# 2. Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionCustomError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


try:
    dividend = int(input("Введите делимое число: "))
    divisor = int(input("Введите делитель: "))
    if divisor is 0:
        raise ZeroDivisionCustomError
    result = int(dividend/divisor)
    print(f"Результат деления {dividend}/{divisor}={result}")
except ZeroDivisionCustomError as e:
    print(e)
