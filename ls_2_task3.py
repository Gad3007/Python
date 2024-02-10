import random

N = int(input("Введите число в диапозоне от 1 до 100 "))
count = 0
maxCount = 0
i = 0
while i < N:
    t = random.randint(-50, 50)
    print(t)
    if t > 0:
        count += 1
        if maxCount < count:
            maxCount = count
    
    else:
        count = 0 
    i += 1
print(maxCount)