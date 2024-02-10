import random

n = 10
m = 10
list_first = [random.randint(1, 10) for _ in range(n)]
list_second = [random.randint(1, 10) for _ in range(m)]
print(list_first , list_second )
r = []
for i in list_first :
    if i not in list_second:
        r.append(i)

print(r)        