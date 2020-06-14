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


#вариант с решением через List

seasons_dict2 = ['зима', 'весна', 'лето', 'осень']
while True:
    user_answer2 = input('введите число месяца')
    if user_answer2.isdigit():
        user_answer2 = int(user_answer2)
        break
    print('Вы ввели не число')

if user_answer2 == 12 or user_answer2 == 1 or user_answer2 == 2:
    print(seasons_dict2[0])
elif user_answer2 == 3 or user_answer2 == 4 or user_answer2 == 5:
    print(seasons_dict2[1])
elif user_answer2 == 6 or user_answer2 == 7 or user_answer2 == 8:
    print(seasons_dict2[2])
elif user_answer2 == 9 or user_answer2 == 10 or user_answer2 == 11:
    print(seasons_dict2[3])



