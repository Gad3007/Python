data = [2, 5, 9, 12, 2, 6, 2, 0]
# ответ 4
count = 0
for i in range(len(data) - 1):
    print(f"{i = }\t{data[i] = }")
    if data[i] < data[i + 1]:
        count += 1
print(count)