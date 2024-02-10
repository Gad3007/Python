# list_1 = [1,2,3,5,8,15,23,38]
# list_2 = []
# for item in range (len(list_1)):
#     if list_1[item] % 2 == 0:
#         list_2.append((list_1[item], list_1[item] ** 2))

# print(list_2)

def select (f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

list_1 = [1,2,3,5,8,15,23,38]
res = map(int, list_1)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)