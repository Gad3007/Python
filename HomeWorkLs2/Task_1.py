# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

coins = [1, 1, 1, 1, 0]
# count1 = 0
# count2 = 0
# for i in coins :
#     if coins[i] == 0 :
#         count1 += 1
#         print(count1)
#     else :
#         count2 += 1
#         print(count2)
# if count2 < count1 :
#     print(count2)
# else:
#     print(count1) 
count1 = 0
count2 = 0
for i in range(len(coins)) :
    if coins[i] == 0 :
        count1 += 1
        print(count1)
    else :
        count2 += 1
        print(count2)
if count2 < count1 :
    print(count2)
else:
    print(count1) 