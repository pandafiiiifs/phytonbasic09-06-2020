#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self,name,size):
        self._name = name
        self._size = size
        self._area = None
    @property
    def get_area(self):
        if self._area is None:
            self._calc()
        return self._area

    @abstractmethod
    def _calc(self):
        pass


    def __add__(self, other):
        self.other = self._size + other._size
        return f'Общий расход ткани {self.other}'


    def __str__(self):
        return f'Название одежды {self._name}\nЕго расход ткани:{self._area}'



class Coat(Clothes):

    def _calc(self):
        self._area = self._size/6.5 + 0.5



class Costume(Clothes):
    def _calc(self):
        self._area = 2 * self._size + 0.3




a = Coat('пальто',52)
a.get_area
print(a)

b = Costume('армани', 190)
b.get_area
print(b)
print(a+b)


