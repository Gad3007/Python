# def fun (a, b):
#     a = int(input('Введите а: '))
#     b = int(input('Введите b: '))
#     result = a ** b 
#     return result

# print(fun(1, 2))

def fun (a, b):
    if b == 0:
        return True
    else:
        return a * fun(a,b-1)
    
print(fun(3, 5))

# def fun (a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * fun(a,b-1)
    
# print(fun(a, b))