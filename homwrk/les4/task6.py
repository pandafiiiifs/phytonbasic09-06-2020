#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""задание а"""
from random import randrange
from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el < 15:
        #print(randrange(el))#случайные числа
        print(el)

    else:
        break



#задание b
from itertools import cycle
my_list = ['eggs', 'spam', 42, False]
for el in cycle(my_list):
  print(el)
    