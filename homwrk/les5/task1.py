file = open('test.txt', 'w', encoding='UTF-8')
user_answer = input('Введите текст\nесли хотите завершить просто нажмите ENTER \n')
while user_answer:
    file.writelines(user_answer)
    user_answer = input('Введите текст\nесли хотите завершить просто нажмите ENTER \n')
    if not user_answer:
        break

file.close()
file = open('test.txt', 'r')
words = file.readlines()
print(words)
file.close()