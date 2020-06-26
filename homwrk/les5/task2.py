my_file = open('test_2.txt', 'r', encoding='UTF-8')
content = my_file.read()
print(f'Содержимое файла:\n{content}')
my_file = open('test_2.txt', 'r')
with open('test_2.txt') as infile:
    lines=0
    words=0
    for line in infile:
        wordslist=line.split()
        lines=lines+1
        words=words+len(wordslist)
print(f'количество строк:\n {lines}')
print(f'количество слов в строке:\n {words}')
