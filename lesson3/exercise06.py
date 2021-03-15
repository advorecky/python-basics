# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(str_1):
    return str_1.capitalize()


def multiple_capitalize(str_1):
    result = ""
    for word in str_1:
        if len(result) == 0:
            result += int_func(word)
        else:
            result += " " + int_func(word)

    return result


user_str = input("Введите слово из маленьких латинских букв: ")
print(int_func(user_str))

user_str = input("Введите строку из слово, состоящих из маленьких латинских букв: ").split()
print(multiple_capitalize(user_str))
