#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class No_null_division(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите положительное число: ")
inp_data_2 = input("Введите положительное число: ")


try:
    inp_data = int(inp_data)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise No_null_division("Нельзя делить на ноль")
except ValueError:
    print("Вы ввели не число")
except No_null_division as err:
    print(err)
else:
    print(f'Все хорошо. Ваше число: ({inp_data/inp_data_2})')