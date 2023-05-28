'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1
'''
from random import randint
size_list=int(input('Введите размер списка '))
namber=int(input('Введите искомое число '))
my_list=[randint(0,10) for i in range(size_list)]
count=0
for i in my_list:
    if i==namber:
        count+=1
print(my_list)
print(f'Число {namber} встречается {count} раз ')
