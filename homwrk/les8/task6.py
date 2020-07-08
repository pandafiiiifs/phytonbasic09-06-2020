#Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class  Warehouse:
    def __init__(self, *args):
        self.my_list = []



class Equipment:
    def __init__(self, name, price, *args):
        self.name = name
        self.price = price
        self.my_list = []
        self.my_list_1 = []
        self.my_dict = {'название модели': self.name, 'цена за шт.': self.price}



    def __str__(self):
        return f'модель {self.name} цена {self.price}'


    def my_input(self):
        try:
            name_1 = input('введите наименование товара')
            price_1 = int(input('введите цену товара'))
            my_dict_1 = {'название модели': name_1, 'цена за шт.': price_1}
            self.my_dict.update(my_dict_1)
            self.my_list.append(self.my_dict)
            print (f'Текущий список -\n {self.my_list}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_list_1.append(self.my_list)
            print(f'Весь склад -\n {self.my_list_1}')
            return f'Выход'
        else:
            return Equipment.my_input(self)







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
a.my_input()
