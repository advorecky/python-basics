# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def replace_words(str, words):
    for key, value in words.items():
        str = str.replace(key, value)
    return str


try:
    with open("exercise04a.txt", encoding="utf-8") as file_a:
        data = []
        thesaurus = {"One": "Один",
                    "Two": "Два",
                    "Three": "Три",
                    "Four": "Четыре"}
        for line in file_a:
            data.append(replace_words(line, thesaurus))

    with open("exercise04b.txt", "w", encoding="utf-8") as file_b:
        file_b.writelines(data)
except IOError:
    print("Произошла ошибка ввода-вывода!")
