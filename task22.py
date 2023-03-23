'''
Даны два неупорядоченных набора целых чисел (может быть, с 
повторениями). Выдать без повторений в порядке возрастания 
все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
 m - кол-во элементов второго множества. Затем пользователь вводит 
 сами элементы множеств.
'''

input_list1 = []
input_list2 = []
list1_len = int(input("Введите количество элементов n "))
list2_len = int(input("Введите количество элементов m "))
for _ in range(list1_len):
    input_list1.append(int(input("Введите число: ")))
print(input_list1)  
for _ in range(list2_len):
    input_list2.append(int(input("Введите число: ")))
print(input_list2)  

a = set(input_list1)
b = set(input_list2)
c = sorted(a.intersection(b))

print(c)