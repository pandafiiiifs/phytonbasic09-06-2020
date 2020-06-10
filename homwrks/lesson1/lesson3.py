#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

user_answer = input( 'введите число')
result = f'{user_answer} + {user_answer*2} + {user_answer*3} '
result2 = f'{int(user_answer) + int(user_answer*2) + int(user_answer*3)}'
result3 = f'{result} = {result2}'
print(result3)