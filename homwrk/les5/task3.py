with open('test_3.txt', 'r', encoding='UTF-8') as my_file:
    salers = []
    money = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           money.append(i[0])
        salers.append(i[1])
print(f'Оклад меньше 20.000 {money}, средний оклад {sum(map(int, salers)) / len(salers)}')