def merge_sorted(list1, list2):
    sort_list = []
    n1 = 0
    n2 = 0
    while len(list1)>n1 or len(list2)>n2:
        if len(list1)==n1:
            sort_list.append(list2[n2])
            n2+=1
        elif len(list2)==n2:
            sort_list.append(list1[n1])
            n1+=1
        elif list1[n1]<=list2[n2]:
            sort_list.append(list1[n1])
            n1+=1
        else:
            sort_list.append(list2[n2])
            n2+=1 
    return sort_list
# Пример 1
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]
print(merge_sorted(a, b))  
# Ожидается: [1, 2, 3, 4, 5, 6, 7, 8, 10]

# Пример 2 (списки разной длины)
c = [1, 2, 3]
d = [4, 5, 6, 7]
print(merge_sorted(c, d))  
# Ожидается: [1, 2, 3, 4, 5, 6, 7]

# Пример 3 (один из списков пустой)
e = []
f = [1, 2, 3]
print(merge_sorted(e, f))  
# Ожидается: [1, 2, 3]

# Пример 4 (равные элементы)
g = [1, 3, 5]
h = [1, 2, 3, 4]
print(merge_sorted(g, h))  
# Ожидается: [1, 1, 2, 3, 3, 4, 5] 