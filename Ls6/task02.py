# Семинар 6. Повторение списков
# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5
# 1 2 3 4 5 
# Вывод: 0 
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2
import random

n = 10
list_first = [random.randint(1, 10) for _ in range(n)]

print(list_first) 
count = 0

for i in range(2, len(list_first)):
    if list_first[i - 2] < list_first[i - 1] and list_first[i] < list_first[i - 1]:
        count +=1
print (count)

