'''
Задача 6.
Дана строка (возможно, пустая), состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку,если на вход пришла невалидная строка.
Пояснения:
Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза,к нему добавляется 
количество повторений
'''
def rle(input_str):
    if not input_str.isalpha():
        return print('Ошибка ввода')
    else:
        result = ""
        last_symb = input_str[0]
        count = 1
        for i in range(1, len(input_str)):
            if input_str[i] == last_symb:
                count+=1
            else:
                result += last_symb
                if count > 1:
                    result += str(count)
                count =1
                last_symb = input_str[i]
        result += last_symb
        if count > 1:
            result += str(count)
    return result


input_str = input("Введите стороку: ").upper()
print(rle(input_str))
