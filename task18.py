'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
'''
from random import randint
size_list=int(input('Введите размер списка '))
namber=int(input('Задайте элемент '))
my_list=[randint(0,10) for i in range(size_list)]
temp=namber-my_list[0]
element=my_list[0]
print(my_list)
print()
for i in my_list:
    if namber>i and namber-i<temp:
        temp=namber-i
        element=i
    elif namber<i and i-namber<temp:
        temp=i-namber
        element=i
print(element)

