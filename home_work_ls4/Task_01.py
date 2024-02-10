# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
# Create an empty list to hold the integers
# var1 = '1 4'
# var2 = '1'
# var3 = '3 4 5 6'
# var1 = '5 5'
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'
print(var2)
var2.split()
print(var2)


a = set(var2.split())
b = set(var3.split())

result = sorted(a.intersection(b))
print(*result) # РАСПАКОВЫВАЕМ СПИСОК **********

# if result == 0:
#     if result[0] == ' ':
#         result.remove(' ')
    
# print(result)
# Create an empty list to hold the integers
# int_list = []

# # Loop through each string in the list
# for string in result:
#     # Convert the string to an integer and append it to the list
#     int_list.append(int(string))

# # Print the list of integers
# print(*int_list)

# var3 = var2.intersection(var3)


# var02 = var2.split(' ')
# var03 = var3.split(' ')

