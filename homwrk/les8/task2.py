#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class No_null_division:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2


    @staticmethod
    def result(num_1, num_2):
        try:
            num_1 = int(num_1)
            num_2 = int(num_2)
            if num_2 == 0:
                return f'Нельзя делить на ноль'
        except ValueError:
            return f'Вы ввели не число'
        except NameError:
            return f'Вы ввели не число'
        else:
            return f'Все хорошо. Ваше число: ({num_1 / num_2})'



a = No_null_division(10,1000)
print(No_null_division.result(10,0))
print(No_null_division.result(10,"wdw"))
print(a.result(1000,10))
