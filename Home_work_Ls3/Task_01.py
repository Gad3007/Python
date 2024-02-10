# list_1 = list()
# x = 0
# count = 0
# for i in range (5):
#     n = int(input())
#     list_1.append(n)
#     if n == 3 :
#         count += 1
# print (list_1)
# print(count)    

list_1 = [1, 5, 5, 4, 5]
k = 5 
count = 0
for i in range(len(list_1)) :
    if k == list_1[i] :
        count += 1
print(list_1)
print(count)
