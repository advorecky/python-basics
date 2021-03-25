# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open("exercise05.txt", "w") as file:
        user_input = input("Введите числа через пробел: ")
        file.writelines(user_input)
        numbers = user_input.split()
        print(sum(map(int, numbers)))
except IOError:
    print("Произошла ошибка ввода-вывода!")
