# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

random_list = [randint(1,300) for x in range(15)]
result_list = []

for i in range(1, len(random_list)):
    if random_list[i] > random_list[i - 1]:
        result_list.append(random_list[i])

print(f"Исходный список: {random_list}")
print(f"Результат: {result_list}")
