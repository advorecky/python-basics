# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open("exercise02.txt") as file:
        file = file.readlines()
        print(f"Количество строк: {len(file)}")
        for index, value in enumerate(file):
            number_of_words = len(value.split())
            print(f"В строке #{index + 1} слов: {number_of_words}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
