#      ^
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr = [5,3,4]


# # print(len(arr) - 1)
# if len(arr) == 1 :
#     sum.append(arr[0])
#     print(max(sum))
# elif len(arr) == 2:
#     sum.append(arr[0]+arr[1])
# else:
#     for i in range (len(arr)):
#         if i == 0 :
#             sum.append(arr[i]+arr[-1]+arr[i+1]) 
#             print(f'Иф{sum}')
#         elif i == (len(arr) - 1):
#             sum.append(arr[i]+arr[i-1]+arr[0])
#             print(f'"KBA"{sum}')
#         else:    
#             sum.append(arr[i]+arr[i+1]+arr[i-1])
#             print(f'елсе{sum}')
# print(max(sum))
arr = [5,3,4]
sum = []
if len(arr) == 1 :
    sum.append(arr[0])
elif len(arr) == 2:
    sum.append(arr[0]+arr[1])
else:
    for i in range (len(arr)):
        if i == 0 :
            sum.append(arr[i]+arr[-1]+arr[i+1]) 
        elif i == (len(arr) - 1):
            sum.append(arr[i]+arr[i-1]+arr[0])
        else:    
            sum.append(arr[i]+arr[i+1]+arr[i-1])
print(max(sum))