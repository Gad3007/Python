s = int(input('s= '))
p = int(input('p= '))

x = 0 
y = 0 
for x in range(s) :
    for y in range (s) :
        if x*y == p and x+y == s and x <= y :
            print (f'Загаданные числа = {x} , {y}')