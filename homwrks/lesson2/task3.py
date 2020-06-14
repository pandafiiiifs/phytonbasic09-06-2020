# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


seasons_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5) , 'лето': (6, 7, 8),'осень': (9, 10, 11)}



while True:
    user_answer = input('введите число месяца')
    if user_answer.isdigit():
        user_answer = int(user_answer)
        break
    print('Вы ввели не число')


for key in seasons_dict.keys():
    if user_answer in seasons_dict[key]:
        print(key)