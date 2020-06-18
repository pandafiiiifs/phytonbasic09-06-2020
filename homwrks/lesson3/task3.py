
#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.



def my_func():
    a = list(map(int, input('введите числа через пробел').split()))
    m1=max(a)
    a.remove(m1)
    m2=max(a)
    sum = m1 + m2
    return sum

b = my_func()
print(b)
