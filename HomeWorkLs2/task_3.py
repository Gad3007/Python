k = 0
n = 0
number = int(input('введите число: '))
while n < number :
    n = 2**k
    if n  <= number :
        print (f'{n}')
        k = k + 1