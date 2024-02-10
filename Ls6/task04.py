def sum_del(num):
    count = 1 # Суммма делителей, начинаем считать со 2 -го
    for i in range(2, int(num ** 0.5) + 1): #для числа 100: 1 2 4 5 10 20 25 50
        if num % i == 0:
            count += i
            if i != num // i:
                count += num // i
    return (count)

for n in range(1, 100_000):
    m = sum_del(n)
    if n < m and (n == sum_del(m)):
        print(n, m)