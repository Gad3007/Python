import random # Импортировать в начале

n = int(input('введите число N: '))
min_ = float('inf')
max_ = float('-inf')

for i in range(1, n + 1):
    mass = random.randint(1,51)
    
    print(f"Арбуз номер {i} имеет массу {mass}")
    if mass > max_:
        max_ = mass
    if mass < min_:
        min_ = mass
        
print (f"max= {max_}, min = {min_}")