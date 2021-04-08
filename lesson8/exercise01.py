# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def convert_date(cls, date_string):
        day, month, year = map(int, date_string.split("-"))
        return day, month, year

    @staticmethod
    def check_date(date_string):
        day, month, year = map(int, date_string.split("-"))
        return day <= 31 and month <= 12 and year <= 2021
