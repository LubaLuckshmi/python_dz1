'''
Задача 3. 
Sample Input
["eat", "tea", "tan", "ate", "nat", “bat"]
Sample Output
[ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
Т. е. сгруппировать слова по "общим буквам".
'''
def group(s):
    d ={}
    for word in s:
        key = "".join(sorted(list(word)))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    result =[]
    for v in d.values():
        result.append(v)
    print(result)

input_str = ["eat", "tea", "tan", "ate", "nat", "bat", "qwer", "rewq", "wate", "tawe", "awet"]
print(input_str)
group(input_str)