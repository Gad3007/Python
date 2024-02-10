def same_by(func, list_1):
     if not list_1:
          return True
     a = func(list_1[0])
     for i in list_1:
        print(i)
        if func(i) != a:         
            return False
        
     return True 


values = []
if same_by(lambda x: x % 2, values):
        print("‘same’")
else:
    print("‘different’")


# def same_by(characterisitc,objects):
#     return len(set(map(characterisitc, objects))) <= 1
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
     
#         print("‘same’")
# else:
#     print("‘different’")

