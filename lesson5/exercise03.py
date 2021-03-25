# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

try:
    with open("exercise03.txt", encoding="utf-8") as file:
        salaries = []
        print("Список сотрудников, имеющих оклад менее 20 тыс.:")
        for line in file:
            last_name, salary = line.split()
            salary = float(salary)
            if salary < 20000:
                print(last_name)
            salaries.append(salary)
        print(
            f"Средняя величина дохода сотрудников: {sum(map(float, salaries)) / len(salaries)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
