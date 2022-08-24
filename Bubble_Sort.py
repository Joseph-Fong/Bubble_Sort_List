list = [5, 2]

size = len(list)
for s in range(size):
    for v in range(size):
        if v >= size-1:
            break
        else:
            if list[v] > list[v+1]:
                x = list[v]
                list[v] = list[v+1]
                list[v+1] = x
print(list)