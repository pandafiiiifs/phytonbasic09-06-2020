# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class  Warehouse:
    def __init__(self, *args):
        self.my_list = []



class Equipment:
    def __init__(self, name, price, *args):
        self.name = name
        self.price = price
        self.my_dict = {'название модели': self.name, 'цена за шт.': self.price}


    def __str__(self):
        return f'модель {self.name} цена {self.price}'




class Printer(Equipment):
    def print (self):
        return f'я принтер по имени {self.name}'



class Scaner(Equipment):
    def print (self):
        return f'я сканер по имени {self.name}'


class Xerox(Equipment):
    def print (self):
        return f'я ксерокс по имени {self.name}'


a = Scaner('HP', 10000)
print(a)
print(a.print())
