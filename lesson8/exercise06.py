# 6. Продолжить работу над вторым заданием. Реализуйте
# механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый
# тип данных.
# Подсказка: постарайтесь по возможности реализовать в
# проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class StorageAppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageAppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить еденицу оргтехники на склад:\n {text}"


class TransferStorageError(StorageAppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оргтехники:\n {text}"


class ValidateEquipmentError(StorageAppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def __str__(self):
        return f"На складе {len(self.__storage)} едениц оргтехники"

    def __getitem__(self, index):
        return self.__storage[index]

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError

        del self.__storage[index]

    def add(self, item: "OfficeEquipment"):
        self.__storage.append(item)

    def transfer(self, index: int, department: str):
        item: OfficeEquipment = self.__storage[index]
        if item.department:
            raise TransferStorageError(
                f"Оборудование {item} уже передано в отдел {item.department}")
        item.department = department


class OfficeEquipment:
    def __init__(self, category: str, vendor: str, model: str, color: str, price: float):
        self.category = category
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price
        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.category} {self.vendor} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__("Printer", *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__("Scanner", *args)


class Copier(OfficeEquipment):
    def __init__(self, *args):
        super().__init__("Copier", *args)
