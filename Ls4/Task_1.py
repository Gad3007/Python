# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

string_ = "a a a b c a a d c d d"
orig = string_.split()
print(orig)

newlist = [] 
count_times = {}

for symbol in orig:
    if not symbol in count_times:
        newlist.append(symbol)
        count_times[symbol] = 1

    else:
        newlist.append(f'{symbol}_{count_times[symbol]}')
        count_times[symbol] += 1

print(" ".join(newlist))
print(count_times)