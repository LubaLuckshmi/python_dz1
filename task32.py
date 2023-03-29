'''
Задача 32: Определить индексы элементов массива (списка), значения 
которых принадлежат заданному диапазону (т.е. не меньше заданного 
минимума и не больше заданного максимума)
'''

import random

some_list = [random.randint(1, 15) for _ in range(10)]

print(some_list)

min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
result_list = []

for i in range(len(some_list)):
    if min <= some_list[i] <= max:
       result_list.append(i)

print(result_list)


