""" Задача 18
Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих строках 
записаны N целых чисел Ai. Последняя строка содержит число X

Пример:
5
1 2 3 4 5
6
-> 5 """

from random import randint
list_length = int(input('Enter the length of the array: '))
requested_number = int(input('To what number do you want to find the closest element in the array: '))
random_list = []
count = 0
num = 0
loop = True
elements_list =[]

while count <= list_length:
    random_list.append(randint(0, 40))
    count += 1
print(random_list)

while loop:
    num += 1
    for i in random_list:
        if i + num == requested_number or i - num == requested_number:
            elements_list.append(i)
            loop = False

if len(elements_list) == 1:
    print(f'The closest number to the requested number "{requested_number}" is {elements_list[0]}')
else:
    print(f'The closest numbers to the requested number "{requested_number}" are {elements_list[0]} and {elements_list[1]}')