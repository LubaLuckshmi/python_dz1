#Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
#величине элемент к заданному числу X. Пользователь в первой 
#строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя 
#строка содержит число X
#*Пример:*
'''
5
    1 2 3 4 5
    6
    -> 5
    '''
input_list = []
list_len = int(input("Введите количество элементов "))
for _ in range(list_len):
    input_list.append(int(input("Введите число: ")))
print(input_list)   

input_X = int(input("Введите число X: "))

min = abs(input_X -input_list[0])
min_index = 0 
for i in range(list_len):
    diff = abs(input_X - input_list[i])
    if diff < min:
        min = diff    
        min_index = i
   
print(input_list[min_index])
