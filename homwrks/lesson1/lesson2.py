#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
while True:
    var_time = input('введите время в секундах')
    if var_time.isdigit():
        var_time = int(var_time)
        break
    print('Вы ввели не число')

result = f'{var_time/3600}:{var_time/60}:{var_time}'
print(result)