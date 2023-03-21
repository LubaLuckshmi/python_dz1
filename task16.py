'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое 
число X в массиве A. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X. 
Попробуйте использовать метод count(), а также решите задачу с 
помощью своего алгоритма (без count). Замерьте время работы двух 
алгоритмов и сравните, подумайте, почему оно отличается.
*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
import time
input_list = []
list_len = int(input("Введите количество элементов "))
for _ in range(list_len):
    input_list.append(int(input("Введите число: ")))
print(input_list)   

input_X = int(input("Введите число X: "))

count = 0
for i in range(list_len):
    if input_list[i] == input_X:
        count +=1

start = time.perf_counter()
print(f"Число {input_X} повторяется {count} раз")
end = time.perf_counter()
first_time = end - start


start = time.perf_counter()
print(input_list.count(input_X))
end = time.perf_counter()
second_time = end - start

print(first_time/second_time)