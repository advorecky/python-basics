# 4. Начните работу над проектом «Склад оргтехники». Создайте
# класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти
# классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие
# для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass


class OfficeEquipment:
    def __init__(self, category: str, vendor: str, model: str, color: str, price: float):
        self.category = category
        self.vendor = vendor
        self.model = model
        self.color = color
        self.price = price

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
