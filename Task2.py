i = int(input('Сколько вагонов прошел Витя: '))
j = int(input('В каком вагоне оказался: '))

output = j + i - 1
#output2 = j   
if i == j :
    print('Недостаточно информации')
else :
    print(f'{output} C хвоста')
        
