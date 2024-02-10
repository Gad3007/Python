n = int(input("Введите число: "))
def simple_number(n):
    count = 0
    for i in range(2,n //2):
        if n % i == 0:
            count = 1
            break
    if count == 1:
        print("No")
    else:
        print("Yes")


a = simple_number(n)

# num = int(input("Введите число: "))
# count = 0

# for i in range(2, num):
#     if num % i == 0:
#         count = count + 1

# if count <= 0:
#     print("Число простое")
# else:
#     print("Число не является простым")

# def numbers(n):
#     result = "Да"
#     for i in range(2, n):
#         if n % i == 0 :
#             result = "Нет"
#             break
#     print(result)

# numbers(14)

# def is_prime(num):
#     count = True

#     for i in range(2, num):
#         if num % i == 0:
#             count = False
#             break

#     if count:
#         return "Число простое"
#     else:
#         return "Число не является простым"


# num = int(input("Введите число: "))
# print(is_prime(num))