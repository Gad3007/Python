# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
#  Пример
# 385916 -> yes
# 123456 -> no

n = int(input('Введите 6-тизначное число'))

n1 = n % 1000
n2 = n // 1000

n21 = n2 % 10  
n22 = n2 % 100 // 10 
n23 = n2 // 100 
n2_res = n21 + n22 + n23 
n11 = n1 % 10  
n12 = n1 % 100 // 10 
n13 = n1 // 100 
n1_res = n11 + n12 + n13 
if n1_res == n2_res :
    print('yes')
else:
    print('no')


