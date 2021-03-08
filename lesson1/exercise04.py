# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

positive_integer = int(input("Введите целое положительное число: "))

# Предположим, что последняя цифра самая большая в числе
max_digit = positive_integer % 10

while positive_integer > 0:
    if positive_integer % 10 > max_digit:
        max_digit = positive_integer % 10
    positive_integer = positive_integer // 10

print(max_digit)
