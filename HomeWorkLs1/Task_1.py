#Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input('Введите трехзначное число: '))
num1 = 0
num2 = 0
num3 = 0
if number > 999 or number < -999 :
    print('Введено не правильное число!')    
else:
    num1 = number % 10  
    num2 = number % 100 // 10 
    num3 = number // 100 
    result = num1 + num2 + num3
    print (f'Cумма чисел = {result}')
    

