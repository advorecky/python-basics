# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

class Storage:
    def __init__(self):
        self.__storage = []

    def __str__(self):
        return f"На складе {len(self.__storage)} едениц оргтехники"

    def __getitem__(self, index):
        return self.__storage[index]

    def add(self, item: "OfficeEquipment"):
        self.__storage.append(item)

    def transfer(self, index: int, department: str):
        item: OfficeEquipment = self.__storage[index]
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
