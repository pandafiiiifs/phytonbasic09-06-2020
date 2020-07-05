 #Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 # который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__()
 # для реализации операции сложения двух объектов класса Matrix (двух матриц).
 # Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно —
 # первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import numpy as np


class Matrix:
    def __init__(self,eye):
        self.eye = eye

    def __add__(self, other):
        return Matrix([[self.eye[i][j] + other.eye[i][j]for j in range(len(self.eye[0]))]for i in range(len(other.eye))])








a = Matrix([[31, 22],
            [37, 43]])
print(a)
b = Matrix([[3, 5],[32, 2, 5]])

print(b)
c = a+b
print(c)