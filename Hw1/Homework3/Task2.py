data = [1, 2, 3, 2, 76, 5, 8, 3, 6, 5, 2, 1, 5]

for i in set(data):
    if data.count(i) == 1:
        data.remove(i)

print(list(set(data)))