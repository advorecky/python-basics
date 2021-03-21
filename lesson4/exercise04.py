# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

random_list = [randint(1, 50) for x in range(15)]
result_list = [el for el in random_list if random_list.count(el) == 1]

print(f"Исходный список: {random_list}")
print(f"Результат: {result_list}")