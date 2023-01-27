from random import randint
import numpy as np


print('------------------------- ПР 6 Вариант 9 ------------------\n'
      '1. Дан одномерный массив, состоящий из N вещественных элементов.'
      ' Ввести массив с клавиатуры.\n Найти и вывести минимальный по модулю элемент.'
      'Вывести массив на экран в обратном порядке.\n')

N = int(input("Введите длину массива: "))
array = []
min_ = 0
for i in range(N):
    num = int(input(f"Введите array[{i}] элемент: "))
    array.append(num)
    min_ = num
    if abs(num) < abs(min_):
        min_ = num
print(f"Минимальное по модулю число: {min_}")
print("Массив в обратном порядке: ", end=' ')
for i in reversed(range(0, N)):
    print(array[i], end=' ')


print('\n2. Даны массивы A и B одинакового размера 10. '
      'Вывести исходные массивы.'
      'Поменять местами их содержимое и вывести в начале элементы '
      'преобразованного массива A, а затем — элементы преобразованного массива B\n')


arrA = [2, 3, 5, 6, 2, 4, 9, 5, 2, 3]
arrB = [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

for i in range(10):
    arrA[i], arrB[i] = arrB[i], arrA[i]

print(f'Массив А: {arrA}')
print(f'Массив B: {arrB}')



print('\n----------------- ПР 7 ВАР 9 -----------------------------------------------------\n'
      '1.Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. '
      'Через сколько таких действий получится нуль?')

def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


c = int(input("Введите число: "))
k = 0
while c > 0:
    c -= f(c)
    k += 1

print("Через " + str(k) + " действий")

print('\n'
      '2.Даны 3 различных массива целых чисел. В каждом массиве найти '
      'произведение элементов и среднеарифметическое значение\n')

array1 = [5,3,2,3,4,42,2,10,22]
array2 = [2,2,2,34,8,54]
array3 = [1,545,2,1]

def count_multi_avg(arr):
    multi = 1
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
        multi = multi * arr[i]
    avg = sum / len(arr)
    return multi, avg

print(count_multi_avg(array1))
print(count_multi_avg(array2))
print(count_multi_avg(array3))


print('---------------------ПР 8 ВАР 9 ----------------------------------\n'
      '1. Для целочисленной квадратной матрицы найти число элементов,'
      'кратных k, и наибольший из этих элементов\n')


n = m = 5
arr = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
print('Введите число для расчета кратности: ')
k = int(input('k ='))
ma = 0
c = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]%k == 0:
            c +=1
            if arr[i][j] > ma:
                ma = arr[i][j]
print(*arr, sep='\n')
print(f'Count {c}')
print(f'Max {ma}')




print('\n2. В данной действительной квадратной матрице порядка n найти'
      'наибольший по модулю элемент. \nПолучить квадратную матрицу порядка\n'
      'n — 1 путем отбрасывания из исходной матрицы строки и столбца, на'
      'пересечении которых расположен элемент с найденным значением.\n')


size = int(input("Введите размер матрицы: "))
a = [] # [[16,125,146][137,52,32][149,58,124]]
print("Начальная матрица:")
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(randint(0, 150)))
        print(b[j], end=' ')
    a.append(b)
    print()
maxi = abs(a[0][0])
nomer_stroki = 0
nomer_stobca = 0
for i in range(size):
    for j in range(size):
        if maxi < abs(a[i][j]):
            maxi = abs(a[i][j])
            nomer_stroki = i
            nomer_stobca = j
print("Максимальное значение: ", maxi)
print('Индекс строки', nomer_stroki) #i-1
print('Индекс столбца', nomer_stobca) #j-1
print("Измененная матрица:")

nomer_stroki2 = size - nomer_stroki
nomer_stobca2 = size - nomer_stobca #убрать все элементы с адресом [nomer_stroki, j] и [i, nomer_stobca]
for i in range(size):
    if i != nomer_stroki:
        for j in range(size):
            if j != nomer_stobca:
                print(a[i][j], end=' ')
        print()


print('\n---------------------ПР 9 ВАР 9 ----------------------------------------\n'
      'Для заданий из практической работы №8 для своего варианта.'
      'Организовать ввод данных (матриц) из файла \n(имя: ФИО_группа_vvod.txt)'
      'И вывод результатов в файл (имя: ФИО_группа_vivod.txt)')



with open('C:\DELETEME\КАНАВСКАЯМК_ЗИТ22М_vvod.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]
print(l)
for i in range(len(l)):
    for j in range(len(l)):
            print(l[i][j], end=' ')
    print()

#size = int(input("Введите размер матрицы: "))
a = [] # [[16,125,146][137,52,32][149,58,124]]
print("Начальная матрица:")
for i in range(len(l)):
    for j in range(len(l)):
            print(l[i][j], end=' ')
    print()
maxi = abs(l[0][0])
nomer_stroki = 0
nomer_stobca = 0
for i in range(len(l)):
    for j in range(len(l)):
        if maxi < abs(l[i][j]):
            maxi = abs(l[i][j])
            nomer_stroki = i
            nomer_stobca = j
print("Максимальное значение: ", maxi)
print('Индекс строки', nomer_stroki) #i-1
print('Индекс столбца', nomer_stobca) #j-1
print("Измененная матрица:")

 #убрать все элементы с адресом [nomer_stroki, j] и [i, nomer_stobca]

file = open('C:\\DELETEME\\КАНАВСКАЯМК_ЗИТ22М_vivod.txt', 'w')

for i in range(len(l)):
    if i != nomer_stroki:
        file.write(f'\n')
        for j in range(len(l)):
            if j != nomer_stobca:
                file.write(f'{l[i][j]} ')
                print(l[i][j], end=' ')
        print()

file.close()





