""" Требуется вычислить, сколько раз встречается некоторое число X 
в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих строках 
записаны N целых чисел Ai. Последняя строка содержит число X.

Пример:
5
1 2 3 4 5
3
-> 1 """

from random import randint
list_length = int(input('Enter the length of the array: '))
requested_number = int(input('What number do you want to find in the array: '))
random_list = []
count = 0
number_count = 0

while count <= list_length:
    random_list.append(randint(0, 20))
    count += 1
print(random_list)

for i in random_list:
    if i == requested_number:
        number_count += 1

if number_count == 0:
    print(f'There is no number {requested_number} in the array')
else:
    print(f'The number "{requested_number}" occurs {number_count} times in the array')