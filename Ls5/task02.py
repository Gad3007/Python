import random
n = int(input("Введите количество оценок:"))
data = [random.randint(1,100) for i in range(n)]
max1 = max(data)
min1 = min(data)
print(data)
for i in range(len(data)):
    if data[i] == max1:
        data[i] = min1
print(data)

# import random
# my_number = []
# for i in range(1,10) :
#     my_number.append(random.randint(1,10))

# max_grade = max(my_number)
# min_grade = min(my_number)

# print(my_number)

# for index in range (len(my_number)):
#     if my_number[index] == max_grade:
#         my_number[index] = min_grade

# print(my_number)

# output = []
# my_max = max(list_)
# my_min = min(list_)
# for elem in list_:
#     if elem == my_max:
#         output.append(my_min)
#     else:
#         output.append(elem)

# print(*output)