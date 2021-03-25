# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    with open("exercise01.txt", "w") as file:
        while True:
            user_input = input(
                "Введите строку с данными (для выхода введите пустую строку): ")
            if not user_input:
                break
            else:
                file.writelines(user_input + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
