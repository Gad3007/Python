import random

n = 10
m = 10
list_first = [random.randint(1, 5) for _ in range(n)]
print(list_first)
count = 0
len_range = len(list_first)
list_first.sort()
print(list_first)
i = 0
while len_range > 0:
    count += list_first.count(list_first[i])//2
    len_range -= list_first.count(list_first[i])
    i += list_first.count(list_first[i])
print(count)

