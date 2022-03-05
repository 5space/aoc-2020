order = [6, 8, 5, 9, 7, 4, 2, 1, 3] + [x for x in range(10, 10001)]

order = [x-1 for x in order]
current = order[0]
for i in range(100000):
    index = order.index(current)
    new = order[:]
    for p in range(index+1, index+4):
        new.remove(order[p%len(order)])
    to_add = [order[p%len(order)] for p in range(index+1, index+4)]
    v = (current-1)%len(order)
    while v in to_add:
        v = (v-1)%len(order)
    ni = new.index(v)
    new = new[:ni+1] + to_add + new[ni+1:]
    current = new[(new.index(current)+1)%len(new)]
    order = new
    if current >= 9500: print(i, current)

index = order.index(1)
print(order[index+1], order[index+2])
# 953 45
# 1758 144