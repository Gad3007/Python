"""""
Числа Фибоначчи 
f(1) = 1 
f(2) = 1
f(n) = f(n-1) + f(n-2)

"""""
n = int(input("ВВедите число: "))
num1 = 0
num2 = 1
count = 2
array = [num1, num2]

while count <= n:
    next_num = num1 + num2
    num1 = num2
    num2 = next_num
    array.append(next_num)

    count += 1


print(array)

if n in array:
    text = "Input num {0} is {1} belong Fibonacci".format(n, array.index(n))
    print(text)
else:
    text = "Input num {0} is {1} dont belong Fibonacci".format(n, -1)
    print(text)

    A = int(input('Ввведите число А: '))
number = 3
f1 = 1
f2 = 1
while f2 < A:
    f1, f2 = f2, f1+f2
    number += 1
if f2 == A:
    print(number)
else:
    print(-1)