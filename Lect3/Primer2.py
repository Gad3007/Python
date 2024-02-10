def sum_str(*args):
    res = ''
    for i in args:
        res += i 
    return res

print(sum_str('q','e', 't'))
print(sum_str('q','e', 't','r','o'))
#print(sum_str(str(1,8,9))) ??????????? как исправить
