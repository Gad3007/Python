n = int(input("Введите количество число: "))

def funs(n):
    if n == 0:
        return " "
    num = input("Введите число: ")
    return f"{funs(n - 1)} {num}" 

print(funs(n))