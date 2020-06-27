rus_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test_4.txt', 'r', encoding='UTF-8') as file_obj, open('test_4_new.txt', 'w') as file_obj_2:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus_translate[i[0]] + '  ' + i[1])
    print(new_file)
    file_obj_2.writelines(new_file)
