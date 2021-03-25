# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджер контекста.

from json import dumps

try:
    with open("exercise07.txt", encoding="utf-8") as file_txt:
        out_json = [{}, {}]
        for line in file_txt.readlines():
            name, form_of_ownership, revenue, costs = line.split()
            out_json[0][name] = float(revenue) - float(costs)

        out_json[1]['average_profit'] = round(sum(
            profit for name, profit in out_json[0].items() if profit > 0) / len(out_json[0]))

    with open("exercise07.json", "w") as file_json:
        file_json.write(dumps(out_json))
except IOError:
    print("Произошла ошибка ввода-вывода!")
